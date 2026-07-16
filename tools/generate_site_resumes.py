from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("DV", FONT_REG))
pdfmetrics.registerFont(TTFont("DV-Bold", FONT_BOLD))

DARK = HexColor("#0d0d0f")
RED = HexColor("#d10d20")
PAPER = HexColor("#f5f2ec")
TEXT = HexColor("#28282c")
MUTED = HexColor("#66666c")
LINE = HexColor("#9b9ba0")


def draw_para(c, text, x, y_top, width, size=9, leading=None, color=TEXT, bold=False):
    leading = leading or size * 1.32
    style = ParagraphStyle(
        "resume",
        fontName="DV-Bold" if bold else "DV",
        fontSize=size,
        leading=leading,
        textColor=color,
        alignment=TA_LEFT,
    )
    p = Paragraph(text, style)
    _, height = p.wrap(width, 800)
    p.drawOn(c, x, y_top - height)
    return y_top - height


def section(c, title, x, y, width):
    c.setFont("DV-Bold", 9.2)
    c.setFillColor(RED)
    c.drawString(x, y, title.upper())
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(x, y - 4, x + width, y - 4)
    return y - 17


def content(lang):
    if lang == "en":
        return {
            "name": "LAPOSHIN VLADISLAV",
            "role": "AI / BACKEND ENGINEER",
            "strap": "LLM SYSTEMS / AGENTS / RAG / PRODUCTION",
            "meta": "3 YEARS 2 MONTHS OF PROJECT EXPERIENCE",
            "profile_t": "PROFILE",
            "profile": "AI-oriented backend engineer building applied software, dialogue assistants and LLM integrations. I work across the full delivery cycle: process analysis, architecture, Python backend, tool and function calling, context enrichment, structured output, quality checks, deployment, logging and production diagnostics.",
            "contact_t": "CONTACT",
            "stack_t": "CORE STACK",
            "expert_t": "KEY EXPERTISE",
            "exp_t": "SELECTED PROJECT EXPERIENCE",
            "edu_t": "EDUCATION",
            "contact": ["Telegram: @rize02", "GitHub: github.com/renosaza", "Portfolio: renosaza.github.io"],
            "stack": ["Python / Java / Rust / SQL", "FastAPI / REST APIs / PostgreSQL / Redis", "Linux / Docker / nginx / CI/CD", "LLM APIs / RAG / Tools / Embeddings"],
            "experts": [
                ("LLM SYSTEMS", "Prompt design, structured output, function/tool calling, agents, context management, RAG, embeddings and evaluation."),
                ("BACKEND", "Python, FastAPI, REST APIs, PostgreSQL, Redis, background jobs, authentication, file processing and integrations."),
                ("INFRASTRUCTURE", "Linux, Docker, nginx, CI/CD, logs, smoke checks, observability and production incident diagnostics."),
                ("DATA & DOCUMENTS", "Tabular data, document workflows, normalization, structured extraction, validation and retrieval pipelines."),
            ],
            "projects": [
                ("AI ASSISTANTS & WORKFLOW AUTOMATION", "PROJECT AND CLIENT WORK", "Dialogue assistants connected to APIs, documents, forms and internal workflows. Tool calling, routing, context handling, prompt templates, structured responses and test scenarios."),
                ("GEOSPATIAL PLATFORM & BATCH GEOCODER", "PRIVATE / INTERNAL PROJECT", "Map-centered operational platform and backend geocoding pipeline for XLSX/XLS/CSV data: address detection, normalization, confidence checks, review flows and production export."),
                ("PARAGON TERMINAL AI KERNEL", "OPEN-SOURCE PROJECT", "Architecture and compiled Rust workspace scaffold for an AI terminal kernel: provider boundary, agent runtime, permissions, session event log, Git visibility and MCP/module layers."),
            ],
            "education": "Far Eastern Federal University (FEFU), Institute of Mathematics and Computer Technologies - currently studying.",
            "footer": "Laposhin Vladislav / 2026",
        }
    return {
        "name": "ЛАПОШИН ВЛАДИСЛАВ",
        "role": "AI / BACKEND-ИНЖЕНЕР",
        "strap": "LLM-СИСТЕМЫ / АГЕНТЫ / RAG / ПРОДАКШЕН",
        "meta": "3 ГОДА 2 МЕСЯЦА ПРОЕКТНОГО ОПЫТА",
        "profile_t": "ПРОФИЛЬ",
        "profile": "AI-ориентированный backend-инженер: разрабатываю прикладные системы, диалоговых ассистентов и LLM-интеграции. Работаю по полному циклу - анализ процесса, архитектура, Python-backend, tools/function calling, обогащение контекста, structured output, проверка качества, деплой, логирование и диагностика в продакшене.",
        "contact_t": "КОНТАКТЫ",
        "stack_t": "ОСНОВНОЙ СТЕК",
        "expert_t": "КЛЮЧЕВАЯ ЭКСПЕРТИЗА",
        "exp_t": "ИЗБРАННЫЙ ПРОЕКТНЫЙ ОПЫТ",
        "edu_t": "ОБРАЗОВАНИЕ",
        "contact": ["Telegram: @rize02", "GitHub: github.com/renosaza", "Портфолио: renosaza.github.io"],
        "stack": ["Python / Java / Rust / SQL", "FastAPI / REST APIs / PostgreSQL / Redis", "Linux / Docker / nginx / CI/CD", "LLM APIs / RAG / Tools / Embeddings"],
        "experts": [
            ("LLM-СИСТЕМЫ", "Промпты, structured output, function/tool calling, агенты, управление контекстом, RAG, эмбеддинги и оценка качества."),
            ("BACKEND", "Python, FastAPI, REST API, PostgreSQL, Redis, фоновые задачи, авторизация, обработка файлов и интеграции."),
            ("ИНФРАСТРУКТУРА", "Linux, Docker, nginx, CI/CD, логи, smoke-проверки, наблюдаемость и диагностика инцидентов в продакшене."),
            ("ДАННЫЕ И ДОКУМЕНТЫ", "Табличные данные, документооборот, нормализация, структурированное извлечение, валидация и retrieval-пайплайны."),
        ],
        "projects": [
            ("AI-АССИСТЕНТЫ И АВТОМАТИЗАЦИЯ", "ПРОЕКТНАЯ И КЛИЕНТСКАЯ РАБОТА", "Диалоговые ассистенты с подключением API, документов, форм и внутренних процессов. Tool calling, маршрутизация, контекст, шаблоны промптов, структурированные ответы и тестовые сценарии."),
            ("ГЕОПЛАТФОРМА И ПАКЕТНЫЙ ГЕОКОДЕР", "ЧАСТНЫЙ / ВНУТРЕННИЙ ПРОЕКТ", "Картографическая операционная платформа и backend-пайплайн для XLSX/XLS/CSV: поиск адресных колонок, нормализация, оценка уверенности, ручная проверка и выгрузка результатов."),
            ("PARAGON - ТЕРМИНАЛЬНОЕ AI-ЯДРО", "OPEN-SOURCE ПРОЕКТ", "Архитектура и компилируемый Rust workspace scaffold: абстракция провайдеров, контур агентов, права tools, журнал сессий, Git-видимость и слои MCP/модулей."),
        ],
        "education": "Дальневосточный федеральный университет (ДВФУ), Институт математики и компьютерных технологий - обучаюсь.",
        "footer": "Лапошин Владислав / 2026",
    }


def build(path, lang):
    d = content(lang)
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4
    c.setTitle(f"Laposhin Vladislav resume ({lang})")
    c.setAuthor("Laposhin Vladislav")
    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(DARK)
    c.rect(0, height - 80, width, 80, fill=1, stroke=0)
    c.setFillColor(RED)
    c.rect(0, 0, 12, height, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("DV-Bold", 21)
    c.drawString(36, height - 46, d["name"])
    c.setFont("DV-Bold", 10.5)
    c.setFillColor(HexColor("#dddddf"))
    c.drawString(36, height - 66, d["role"])
    c.setFont("DV-Bold", 8)
    c.setFillColor(white)
    c.drawRightString(width - 36, height - 44, d["strap"])
    c.setFont("DV", 8)
    c.setFillColor(HexColor("#dddddf"))
    c.drawRightString(width - 36, height - 63, d["meta"])

    x0, x1, colw = 36, 315, 244
    y = height - 105
    y = section(c, d["profile_t"], x0, y, width - 72)
    y = draw_para(c, d["profile"], x0, y, width - 72, 9.3, 12.2) - 13

    yl = section(c, d["contact_t"], x0, y, colw)
    yl = draw_para(c, "<br/>".join(d["contact"]), x0, yl, colw, 9.2, 15)
    yr = section(c, d["stack_t"], x1, y, colw)
    yr = draw_para(c, "<br/>".join(d["stack"]), x1, yr, colw, 9.0, 14.5)
    y = min(yl, yr) - 13

    y = section(c, d["expert_t"], x0, y, width - 72)
    positions = [(x0, y), (x1, y), (x0, y - 66), (x1, y - 66)]
    bottoms = []
    for (title, body), (xx, yy) in zip(d["experts"], positions):
        c.setFont("DV-Bold", 8.7)
        c.setFillColor(DARK)
        c.drawString(xx, yy, title)
        bottoms.append(draw_para(c, body, xx, yy - 10, colw, 7.9, 10.2, MUTED))
    y = min(bottoms) - 12

    y = section(c, d["exp_t"], x0, y, width - 72)
    for title, tag, body in d["projects"]:
        c.setFont("DV-Bold", 8.5)
        c.setFillColor(DARK)
        c.drawString(x0, y, title)
        c.setFont("DV-Bold", 6.8)
        c.setFillColor(RED)
        c.drawRightString(width - 36, y, tag)
        y = draw_para(c, body, x0, y - 9, width - 72, 7.7, 9.7, HexColor("#45454a")) - 8

    y = section(c, d["edu_t"], x0, y, width - 72)
    draw_para(c, d["education"], x0, y, width - 72, 8.2, 10.5)

    c.setFillColor(DARK)
    c.rect(0, 0, width, 30, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("DV-Bold", 8)
    c.drawString(36, 11, d["footer"])
    c.setFont("DV", 8)
    c.setFillColor(HexColor("#e5e5e7"))
    c.drawRightString(width - 36, 11, "Telegram @rize02")
    c.save()


if __name__ == "__main__":
    build(ROOT / "renosaza_resume.pdf", "en")
    build(ROOT / "renosaza_resume_ru.pdf", "ru")
