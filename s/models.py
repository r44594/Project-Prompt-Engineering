from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# הגדרת רמות עדיפות למשימה
class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# הגדרת המבנה של משימה בודדת
class Task(BaseModel):
    title: str = Field(..., description="כותרת המשימה")
    description: Optional[str] = Field(None, description="תיאור קצר של המשימה")
    priority: Priority = Field(Priority.MEDIUM, description="רמת עדיפות")
    is_completed: bool = False