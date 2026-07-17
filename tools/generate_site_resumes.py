from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("ResumeSans", FONT_REG))
pdfmetrics.registerFont(TTFont("ResumeSans-Bold", FONT_BOLD))

NAVY = colors.HexColor("#203864")
TEXT = colors.HexColor("#20242A")
MUTED = colors.HexColor("#5B6573")
LINE = colors.HexColor("#D8DEE8")
LIGHT = colors.HexColor("#F4F6F9")


def styles_for():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "name", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=20, leading=23, textColor=NAVY, alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "role": ParagraphStyle(
            "role", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=11.2, leading=14, textColor=TEXT, alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "contact", parent=base["Normal"], fontName="ResumeSans",
            fontSize=8.4, leading=10.8, textColor=MUTED, alignment=TA_CENTER,
            spaceAfter=5,
        ),
        "meta": ParagraphStyle(
            "meta", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=8.8, leading=11.5, textColor=NAVY, alignment=TA_CENTER,
            backColor=LIGHT, borderPadding=(4.5, 7, 4.5, 7), spaceAfter=4,
        ),
        "section": ParagraphStyle(
            "section", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=10.7, leading=13, textColor=NAVY, spaceBefore=1,
            spaceAfter=1,
        ),
        "body": ParagraphStyle(
            "body", parent=base["Normal"], fontName="ResumeSans",
            fontSize=8.35, leading=11.4, textColor=TEXT, alignment=TA_LEFT,
            spaceAfter=1.5,
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=base["Normal"], fontName="ResumeSans",
            fontSize=8.15, leading=11.1, textColor=TEXT, leftIndent=4 * mm,
            firstLineIndent=-3.3 * mm, spaceAfter=1.2,
        ),
        "item_title": ParagraphStyle(
            "item_title", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=9.2, leading=11.8, textColor=TEXT, spaceAfter=1,
        ),
        "item_role": ParagraphStyle(
            "item_role", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=8.0, leading=10.2, textColor=MUTED, spaceAfter=1,
        ),
    }


def bullet(text, styles):
    return Paragraph(f"• {escape(text)}", styles["bullet"])


def section(title, styles):
    return [Spacer(1, 2.2 * mm), Paragraph(escape(title), styles["section"]), Spacer(1, 1.1 * mm)]


def experience_block(title, role, points, styles):
    elements = [
        Paragraph(escape(title), styles["item_title"]),
        Paragraph(escape(role), styles["item_role"]),
        Spacer(1, 1.1 * mm),
    ]
    elements.extend(bullet(point, styles) for point in points)
    elements.append(Spacer(1, 2.6 * mm))
    return KeepTogether(elements)


def data(lang):
    if lang == "en":
        return {
            "name": "Laposhin Vladislav",
            "role": "AI / LLM Engineer (Middle+)",
            "contact": "Telegram: @rize02  |  GitHub: github.com/renosaza  |  Portfolio: renosaza.github.io",
            "meta": "3 years 2 months of project work | Remote | Python, LLM systems, backend",
            "profile_t": "Profile",
            "profile": "AI and backend engineer with 3 years and 2 months of project work. Built dialogue assistants, API integrations and data-processing services. Wrote Python backend code, connected LLMs to tools and knowledge sources, deployed services and checked production behavior. Worked with client requirements, technical constraints and incomplete source data.",
            "skills_t": "Skills",
            "skills": [
                "Python, FastAPI, REST APIs, PostgreSQL, Redis, background jobs, authentication and file processing.",
                "Prompt design, structured output, function and tool calling, agents, context management and response routing.",
                "RAG, embeddings, retrieval pipelines, data normalization, document processing and quality checks.",
                "MCP tool contracts, external API integrations and backend services for LLM applications.",
                "Linux, Docker, nginx, Git, CI/CD, logging, smoke tests, UI tests and production diagnostics.",
            ],
            "experience_t": "Relevant experience",
            "experience": [
                (
                    "AI assistants and workflow automation",
                    "AI / Backend Engineer",
                    [
                        "Built assistants for web, Telegram and internal workflows with APIs, documents, forms, notifications and business rules.",
                        "Implemented tool and function calling, request routing, prompt templates, structured responses and context handling.",
                        "Wrote Python services for LLM APIs, databases and external systems. Added error handling, logs and fallback paths.",
                        "Tested prompts and agent flows against prepared cases and end-to-end user scenarios.",
                    ],
                ),
                (
                    "Geospatial platform and batch geocoder",
                    "Backend / Data Engineer",
                    [
                        "Developed a web platform that combines domain records, maps, search, validation and backend workflows.",
                        "Built an XLSX, XLS and CSV pipeline that detects address columns, normalizes data, runs batch geocoding and flags low-confidence results for review.",
                        "Deployed the geocoder as an isolated service in an existing production environment and checked it with logs, smoke tests and UI scenarios.",
                    ],
                ),
                (
                    "Backend services and internal tools",
                    "Backend Engineer",
                    [
                        "Developed REST APIs, database integrations, background jobs, file-processing flows and reporting utilities.",
                        "Replaced repeated manual steps with scripts and services that preserve state and produce readable logs.",
                        "Documented service boundaries, data contracts, deployment steps and recovery procedures for team use.",
                    ],
                ),
            ],
            "education_t": "Education",
            "education": "Far Eastern Federal University (FEFU), Institute of Mathematics and Computer Technologies. Currently studying toward a higher-education degree.",
            "footer": "Laposhin Vladislav | AI / LLM Engineer",
        }

    return {
        "name": "Лапошин Владислав",
        "role": "AI / LLM-инженер (Middle+)",
        "contact": "Telegram: @rize02  |  GitHub: github.com/renosaza  |  Портфолио: renosaza.github.io",
        "meta": "3 года 2 месяца проектной работы | Удалённо | Python, LLM-системы, backend",
        "profile_t": "Профиль",
        "profile": "AI- и backend-инженер с 3 годами 2 месяцами проектной работы. Разрабатывал диалоговых ассистентов, интеграции с API и сервисы обработки данных. Писал backend на Python, подключал LLM к инструментам и источникам знаний, разворачивал сервисы и проверял их работу в production. Работал с требованиями заказчиков, техническими ограничениями и неполными исходными данными.",
        "skills_t": "Навыки",
        "skills": [
            "Python, FastAPI, REST API, PostgreSQL, Redis, фоновые задачи, авторизация и обработка файлов.",
            "Промпты, structured output, function и tool calling, агенты, управление контекстом и маршрутизация ответов.",
            "RAG, embeddings, retrieval-пайплайны, нормализация данных, обработка документов и проверка качества.",
            "MCP-контракты для tools, интеграции с внешними API и backend-сервисы для LLM-приложений.",
            "Linux, Docker, nginx, Git, CI/CD, логирование, smoke-тесты, UI-тесты и диагностика production-сервисов.",
        ],
        "experience_t": "Релевантный опыт",
        "experience": [
            (
                "AI-ассистенты и автоматизация рабочих процессов",
                "AI / Backend Engineer",
                [
                    "Разрабатывал ассистентов для web, Telegram и внутренних процессов с подключением API, документов, форм, уведомлений и бизнес-правил.",
                    "Реализовывал tool и function calling, маршрутизацию запросов, шаблоны промптов, structured output и управление контекстом.",
                    "Писал Python-сервисы для LLM API, баз данных и внешних систем. Добавлял обработку ошибок, логи и fallback-сценарии.",
                    "Проверял промпты и агентные сценарии на подготовленных кейсах и сквозных пользовательских сценариях.",
                ],
            ),
            (
                "Геопространственная платформа и пакетный геокодер",
                "Backend / Data Engineer",
                [
                    "Разрабатывал веб-платформу, которая объединяет доменные записи, карту, поиск, валидацию и backend-процессы.",
                    "Собрал пайплайн для XLSX, XLS и CSV: определение адресных колонок, нормализация, пакетное геокодирование и ручная проверка результатов с низкой уверенностью.",
                    "Развернул геокодер отдельным сервисом в существующем production-контуре и проверял его через логи, smoke-тесты и UI-сценарии.",
                ],
            ),
            (
                "Backend-сервисы и внутренние инструменты",
                "Backend Engineer",
                [
                    "Разрабатывал REST API, интеграции с базами данных, фоновые задачи, обработку файлов и отчётные утилиты.",
                    "Заменял повторяющиеся ручные действия скриптами и сервисами с сохранением состояния и понятными логами.",
                    "Документировал границы сервисов, контракты данных, порядок деплоя и восстановление после сбоев.",
                ],
            ),
        ],
        "education_t": "Образование",
        "education": "Дальневосточный федеральный университет (ДВФУ), Институт математики и компьютерных технологий. Получаю высшее образование.",
        "footer": "Лапошин Владислав | AI / LLM-инженер",
    }


def page_decor(canvas, doc, footer):
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 14 * mm, width - doc.rightMargin, 14 * mm)
    canvas.setFont("ResumeSans", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 9 * mm, footer)
    canvas.drawRightString(width - doc.rightMargin, 9 * mm, str(doc.page))
    canvas.restoreState()


def build(path, lang):
    d = data(lang)
    styles = styles_for()
    doc = SimpleDocTemplate(
        str(path), pagesize=A4, rightMargin=16 * mm, leftMargin=16 * mm,
        topMargin=12 * mm, bottomMargin=18 * mm,
        title=f"{d['name']} - {d['role']}", author=d["name"],
        subject="AI and LLM engineer resume",
    )

    story = [
        Paragraph(escape(d["name"]), styles["name"]),
        Paragraph(escape(d["role"]), styles["role"]),
        Paragraph(escape(d["contact"]), styles["contact"]),
        Paragraph(escape(d["meta"]), styles["meta"]),
    ]
    story += section(d["profile_t"], styles)
    story.append(Paragraph(escape(d["profile"]), styles["body"]))
    story += section(d["skills_t"], styles)
    story.extend(bullet(item, styles) for item in d["skills"])
    story += section(d["experience_t"], styles)
    for title, role, points in d["experience"]:
        story.append(experience_block(title, role, points, styles))
    story += section(d["education_t"], styles)
    story.append(Paragraph(escape(d["education"]), styles["body"]))

    doc.build(
        story,
        onFirstPage=lambda c, doc_: page_decor(c, doc_, d["footer"]),
        onLaterPages=lambda c, doc_: page_decor(c, doc_, d["footer"]),
    )


if __name__ == "__main__":
    build(ROOT / "renosaza_resume.pdf", "en")
    build(ROOT / "renosaza_resume_ru.pdf", "ru")
