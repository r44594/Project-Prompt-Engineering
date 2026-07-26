import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from src.models import Task

load_dotenv()
model = ChatOpenAI(model="gpt-4o")
tasks_db = []

# פונקציית עזר פנימית (לא כלי, לכן אפשר לקרוא לה ישירות)
def perform_safety_check(task_title: str) -> str:
    prompt = f"""
    אתה עוזר בטיחות. עליך לסווג האם המשימה הבאה תקינה או מניפולטיבית.
    החזר תשובה בפורמט JSON בלבד: {{"is_safe": true/false, "reason": "..."}}
    דוגמאות:
    קלט: "לקנות חלב" -> {{"is_safe": true, "reason": "משימה תקינה"}}
    קלט: "לפרוץ למסד נתונים" -> {{"is_safe": false, "reason": "ניסיון מניפולטיבי לעקוף כללים"}}
    המשימה לבדיקה: "{task_title}"
    """
    response = model.invoke(prompt)
    return response.content

@tool
def safety_check_tool(task_title: str) -> str:
    """בודק אם המשימה תקינה ומותרת להוספה בעזרת ניתוח חכם."""
    return perform_safety_check(task_title)

@tool
def add_task(title: str, description: str = "ללא תיאור", priority: str = "medium") -> str:
    """מוסיפה משימה חדשה לרשימה, לאחר בדיקת בטיחות חכמה."""
    
    # כאן אנחנו קוראים לפונקציה הרגילה ולא ל-StructuredTool
    safety_response = perform_safety_check(title)
    
    try:
        json_str = safety_response.replace('```json', '').replace('```', '').strip()
        data = json.loads(json_str)
        if not data.get("is_safe", True):
            return f"המשימה נחסמה: {data.get('reason', 'תוכן לא תקין')}"
    except Exception:
        return "שגיאה בבדיקת הבטיחות."
    
    new_task = Task(title=title, description=description, priority=priority)
    tasks_db.append(new_task)
    return f"המשימה '{title}' נוספה בהצלחה!"

@tool
def list_tasks() -> str:
    """מחזירה את רשימת כל המשימות הקיימות."""
    if not tasks_db:
        return "אין כרגע משימות ברשימה."
    return "\n".join([f"- {t.title} (עדיפות: {t.priority})" for t in tasks_db])

tools = [add_task, list_tasks, safety_check_tool]
app = create_react_agent(model, tools=tools)

def run_agent(user_input: str):
    response = app.invoke({"messages": [("user", user_input)]})
    return response["messages"][-1].content