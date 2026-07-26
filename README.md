<div align="center">

# Project Prompt Engineering
### *An Intelligent Natural Language → CLI Command Engine with Isolated Execution Capabilities*

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/LLM-OpenAI%20API-412991?style=flat-square&logo=openai&logoColor=white)](https://platform.openai.com/)
[![Gradio](https://img.shields.io/badge/UI-Gradio-FF7C00?style=flat-square)](https://www.gradio.app/)
[![Docker](https://img.shields.io/badge/Sandbox-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![uv](https://img.shields.io/badge/Package%20Manager-uv-DE5FE9?style=flat-square)](https://astral.sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

`Cmdify` is an advanced AI agent designed to bridge the gap between human natural language and terminal execution environments. Developed through **Iterative Prompt Engineering**, it translates complex user intent into precise, syntactically accurate CLI commands — while prioritizing system safety, input validation, and secure execution.

</div>

---

## 📑 Table of Contents

- [Core Features](#-core-features)
- [Interface Preview](#-interface-preview)
- [Tech Stack](#-tech-stack)
- [Quickstart Guide](#-quickstart-guide)
- [🇮🇱 המשך בעברית — תהליך הנדסת הפרומפטים](#-nl--cli-agent--פרויקט-prompt-engineering)

---

## ✨ Core Features

| | תכונה | תיאור |
|---|---|---|
| 💬 | **Natural Language Processing** | Seamlessly converts plain-text instructions into ready-to-execute single-line shell commands. |
| 🖥️ | **Interactive Web Interface** | Modern, user-friendly UI built with **Gradio** for real-time command generation and testing. |
| 🔒 | **Safety & Risk Mitigation** | Embedded guardrails and parsing rules to detect, isolate, and restrict potentially harmful system operations. |
| 🐳 | **Docker Sandbox Execution** | Safely executes and evaluates generated commands within an isolated Docker container, protecting the host operating system. |
| 📊 | **Empirical Performance Tracking** | Benchmarked using dedicated test suites to track accuracy, syntax validity, and safety compliance across prompt iterations. |

---

## 📸 Interface Preview

Below is a demonstration of Cmdify's core workflow and security features:

**1. Translation Input Pipeline**
The primary interface for submitting natural language queries (e.g., file system manipulation requests).

---

## 🧩 Tech Stack

| רכיב | טכנולוגיה |
|---|---|
| **LLM Engine** | OpenAI API |
| **User Interface Framework** | Gradio |
| **Isolation Container** | Docker |

---

## 🚀 Quickstart Guide

### Prerequisites

Ensure the following tools are installed on your environment:

- [Python 3.10+](https://www.python.org/)
- [`uv`](https://astral.sh/uv) (Next-generation Python package manager)
- [Docker Engine](https://www.docker.com/) (Required for sandboxed execution)

### Installation & Setup

**1. Clone the Repository:**
```bash
git clone https://github.com/ay213-git/AI-CLI-Agent.git
cd AI-CLI-Agent
```

---
---

<div align="right">

## 🇮🇱 NL → CLI Agent — פרויקט Prompt Engineering

המטרה המרכזית של הפרויקט היא **תהליך הנדסת הפרומפטים**: Agent שממיר עבור Windows CLI הוראה בשפה טבעית (עברית/אנגלית) לפקודת CLI אחת מדויקת.
התהליך מתבסס על מתודולוגיה איטרטיבית: **לכתוב → להריץ → למדוד → לשפר → לחזור** (לפחות 3 איטרציות).

---

### 🖥️ דרישות מערכת

- Windows 10/11
- Python 3.12+
- `uv` — התקנה:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### ⚙️ התקנה

```bash
uv sync
copy .env.example .env
# ערכי את קובץ ה-.env והכניסי את OPENAI_API_KEY שלך, GOOGLE_SHEET_ID, ונתיב ל-service account JSON
```

---

### 📊 הגדרת Google Sheets

1. צרי project ב־[Google Cloud Console](https://console.cloud.google.com/), הפעילי בו את Google Sheets API.
2. צרי Service Account ← Keys ← Add Key ← JSON. הורידי את הקובץ ושמרי אותו בשם `service-account.json` בשורש הפרויקט.
3. צרי Google Sheet חדש, שתפי אותו עם כתובת המייל של ה-Service Account (בהרשאת **Editor**).
4. העתיקי את ה־`URL` של ה־Sheet אל `GOOGLE_SHEET_ID` בתוך קובץ ה־`.env`.

---

### 🗂️ מבנה הפרויקט

```bash
prompts/                     # אחסון גרסאות הפרומפט (v1, v2, v3 – אחת לכל איטרציה)
scenarios/test_cases.json    # תרחישי בדיקה משותפים לכל האיטרציות – 18 תרחישים
src/agent.py                 # קריאה ל-OpenAI + טעינת הפרומפט לפי גרסה
src/safety.py                # סיווג בטיחות דו-שכבתי (BLOCKED / REQUIRES_CONFIRMATION / SAFE)
src/sheets.py                # רישום אוטומטי ל-Google Sheets (גיליון נפרד לכל איטרציה)
app.py                        # Gradio: ריצה בודדת + "Run all scenarios"
docs/failures.md              # תיעוד הכשלים והשינויים בין איטרציות
```

---

### 🔁 איך לעבוד באיטרציות

1. ודאי ש־`prompts/v1_initial.md` הוא הפרומפט הנוכחי.
2. ב־Gradio, בטאב **"ריצת אצווה"** ← בחרי `v1` + איטרציה `1` ← לחצי **"הרץ את כל התרחישים"**.
3. כל 18 התרחישים נכתבים אוטומטית לגיליון `iter_1` בגוגל שיט.
4. ב־Sheet, מלאי ידנית את עמודות הציון: `format_score`, `syntax_score`, `safety_score`, `overall`, `notes`.
5. כתבי ב־`docs/failures.md` פסקה קצרה: מה נכשל, ואיזה **שינוי יחיד** את מבצעת בעקבותיו.
6. צרי `prompts/v2_refined.md` הכולל את השינוי הזה בלבד. חזרי על שלבים 2–5 עבור איטרציה 2, ולאחר מכן איטרציה 3.

> 🏅 **כלל זהב:** שינוי אחד בכל איטרציה — אחרת לא ניתן לדעת איזה שינוי גרם לאיזה אפקט.

---

### 🛡️ בטיחות

המודל מתבקש בפרומפט להימנע מפקודות הרסניות — אך המערכת **אינה סומכת על כך בלבד**. לאחר כל קריאה, `src/safety.py` סורק את הפלט מול רשימת ביטויים רגולריים (regex) ומסווג אותו:

| רמת סיכון | סטטוס | דוגמאות פקודות |
|---|---|---|
| 🔴 | **BLOCKED** | `rm -rf`, `format`, `shutdown`, `diskpart` וכו' |
| 🟡 | **REQUIRES_CONFIRMATION** | `move`, `taskkill /f`, `net user`, `cmd /c`, `iex` וכו' |
| 🟢 | **SAFE** | כל פקודה שלא זוהתה כמסוכנת או כדורשת אישור |

</div>

---

<div align="center">

נוצר ע"י **רבקי טולידאנו** ✨

</div>
