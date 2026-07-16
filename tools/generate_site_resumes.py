from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

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


def p(text, style):
    return Paragraph(text, style)


def bullet(text, styles):
    return Paragraph(f"• {escape(text)}", styles["bullet"])


def role_block(title, role, bullets, styles):
    items = [
        Paragraph(escape(title), styles["project_title"]),
        Paragraph(escape(role), styles["project_role"]),
        Spacer(1, 1.5 * mm),
    ]
    items.extend(bullet(item, styles) for item in bullets)
    items.append(Spacer(1, 3.3 * mm))
    return KeepTogether(items)


def section(title, styles):
    return [
        Spacer(1, 2.5 * mm),
        Paragraph(escape(title), styles["section"]),
        Spacer(1, 1.4 * mm),
    ]


def styles_for():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "name", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=21, leading=24, textColor=NAVY, alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "role": ParagraphStyle(
            "role", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=11.5, leading=14, textColor=TEXT, alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "contact", parent=base["Normal"], fontName="ResumeSans",
            fontSize=8.7, leading=11, textColor=MUTED, alignment=TA_CENTER,
            spaceAfter=5,
        ),
        "summary_meta": ParagraphStyle(
            "summary_meta", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=9.2, leading=12, textColor=NAVY, alignment=TA_CENTER,
            backColor=LIGHT, borderPadding=(5, 8, 5, 8), spaceBefore=2,
            spaceAfter=5,
        ),
        "section": ParagraphStyle(
            "section", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=11.2, leading=14, textColor=NAVY, borderColor=LINE,
            borderWidth=0, borderPadding=0, spaceBefore=1, spaceAfter=1,
        ),
        "body": ParagraphStyle(
            "body", parent=base["Normal"], fontName="ResumeSans",
            fontSize=8.75, leading=12.2, textColor=TEXT, alignment=TA_LEFT,
            spaceAfter=2,
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=base["Normal"], fontName="ResumeSans",
            fontSize=8.55, leading=11.7, textColor=TEXT, leftIndent=4 * mm,
            firstLineIndent=-3.3 * mm, spaceAfter=1.4,
        ),
        "project_title": ParagraphStyle(
            "project_title", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=9.6, leading=12.3, textColor=TEXT, spaceAfter=1,
        ),
        "project_role": ParagraphStyle(
            "project_role", parent=base["Normal"], fontName="ResumeSans-Bold",
            fontSize=8.2, leading=10.5, textColor=MUTED, spaceAfter=1,
        ),
    }


def data(lang):
    if lang == "en":
        return {
            "name": "Laposhin Vladislav",
            "role": "AI / LLM Engineer (Middle+)",
            "contact": "Telegram: @rize02  |  GitHub: github.com/renosaza  |  Portfolio: renosaza.github.io",
            "meta": "3 years 2 months of cumulative project experience | Remote work | Full delivery cycle",
            "profile_t": "Professional profile",
            "profile": "AI-focused backend engineer with 3 years and 2 months of cumulative project experience. I design dialogue assistants and LLM systems, connecting models to APIs, documents, knowledge bases and internal services. I work across the full cycle: business-process analysis and hypothesis validation, architecture, production-ready Python backend, tools/function calling, RAG and context enrichment, structured output, quality testing, deployment, logging and production diagnostics.",
            "skills_t": "Core competencies",
            "skills": [
                "LLM and agents: prompt engineering, structured output, function/tool calling, agent chains, context and memory management, routing and fallback scenarios.",
                "RAG and data: embeddings, retrieval, data preparation and normalization, chunking/indexing architecture, knowledge-base quality evaluation and structured extraction.",
                "Backend: Python, FastAPI, REST APIs, PostgreSQL, Redis, background jobs, authentication, integrations, file and document processing.",
                "MCP and tools: design of tool layers, MCP integrations and contracts between agents, external services and user interfaces.",
                "Reliability: Linux, Docker, nginx, CI/CD, logging, smoke and UI testing, observability, incident diagnostics, safe deployment and rollback.",
                "Communication: architecture documentation, decomposition of unclear requirements, solution alignment with stakeholders and transfer of technical context to a team.",
            ],
            "experience_t": "Project experience - 3 years 2 months",
            "projects_page1": [
                (
                    "AI assistants and workflow automation",
                    "AI / Backend Engineer",
                    [
                        "Designed dialogue assistants for web, Telegram and internal workflows with APIs, documents, forms, notifications and business logic.",
                        "Implemented tool/function calling, request routing, context management, prompt templates and structured responses.",
                        "Developed Python backend components and integrations with LLM APIs, databases and external services, including error handling and controlled fallbacks.",
                        "Validated quality with test sets and end-to-end user scenarios, versioned changes, logged behavior and analyzed unstable responses.",
                    ],
                ),
                (
                    "Geospatial platform and batch geocoder",
                    "Backend / Data / AI Engineer",
                    [
                        "Developed an operational web platform combining domain records, maps, search, validation and backend workflows for analysis and coordination.",
                        "Built an XLSX/XLS/CSV processing pipeline with automatic address-column detection, normalization, batch processing, confidence scoring and manual-review flows.",
                        "Worked with large exports, quality validation and safe deployment of an isolated service inside an existing production environment.",
                        "Used Linux, Docker and nginx with logging, smoke and UI checks, diagnosing data and infrastructure issues without disrupting the main product.",
                    ],
                ),
            ],
            "experience_cont_t": "Project experience - continued",
            "projects_page2": [
                (
                    "Paragon - terminal AI kernel and agent architecture",
                    "Project Author / Rust Engineer",
                    [
                        "Designed a modular terminal-first AI kernel architecture for cloud and local models, native coding agents and pluggable tools.",
                        "Prepared a compiling Rust workspace scaffold with clear provider, agent, Git, storage, TUI and module boundaries.",
                        "Defined tool permissions, session event logging, pause/resume/interrupt behavior, Git diff visibility and MCP/custom-profile/sandbox/approval layers.",
                        "Documented architecture decisions, module contracts, risks and implementation order; the project is under active staged development.",
                    ],
                ),
                (
                    "Backend services and internal tools",
                    "Backend Engineer",
                    [
                        "Built REST APIs, service components, PostgreSQL/Redis integrations, background jobs, file-processing flows, administrative utilities and reporting pipelines.",
                        "Automated repetitive operations and connected fragmented tools into reproducible workflows with explicit logs and state.",
                        "Supported the complete user path from requirements and data models to deployment, verification and failure recovery.",
                    ],
                ),
            ],
            "tech_t": "Technologies",
            "tech": [
                "Core: Python, FastAPI, SQL, PostgreSQL, Redis, REST APIs, Linux, Docker, nginx, Git, CI/CD, Bash.",
                "AI / LLM: LLM APIs, prompt engineering, structured output, function/tool calling, RAG, embeddings, agents, memory/context, MCP, Ollama and local inference.",
                "Additional: Java, Rust, tabular and document processing, geospatial systems, data validation, observability and architecture documentation.",
            ],
            "education_t": "Education",
            "education": "Far Eastern Federal University (FEFU), Institute of Mathematics and Computer Technologies - currently studying toward a higher-education degree.",
            "extra_t": "Additional information",
            "extra": [
                "Open profile and projects: github.com/renosaza; technical portfolio: renosaza.github.io.",
                "I prefer tasks where an LLM is part of a measurable product: assistants, automation, knowledge retrieval, document processing and internal platforms.",
                "I work beyond prompts, treating data, backend, integrations, security, deployment and observability as one system boundary.",
            ],
            "footer": "Laposhin Vladislav - AI / LLM Engineer",
        }

    return {
        "name": "Лапошин Владислав",
        "role": "AI / LLM-инженер (Middle+)",
        "contact": "Telegram: @rize02  |  GitHub: github.com/renosaza  |  Портфолио: renosaza.github.io",
        "meta": "Опыт: 3 года 2 месяца (проектная разработка) | Удалённая работа | Полный цикл разработки",
        "profile_t": "Профессиональный профиль",
        "profile": "AI-ориентированный backend-инженер с 3 годами 2 месяцами совокупного проектного опыта. Проектирую диалоговых ассистентов и LLM-системы, связываю модели с API, документами, базами знаний и внутренними сервисами. Работаю по полному циклу: анализ бизнес-процесса и гипотезы, архитектура, production-ready Python-backend, tools/function calling, RAG и обогащение контекста, structured output, тестирование качества, деплой, логирование и диагностика в продакшене.",
        "skills_t": "Ключевые компетенции",
        "skills": [
            "LLM и агенты: prompt engineering, structured output, function/tool calling, агентные цепочки, управление контекстом и memory, маршрутизация, fallback-сценарии.",
            "RAG и данные: эмбеддинги, retrieval, подготовка и нормализация данных, chunking/indexing на уровне архитектуры, оценка качества базы знаний, структурированное извлечение.",
            "Backend: Python, FastAPI, REST API, PostgreSQL, Redis, фоновые задачи, авторизация, интеграции, обработка файлов и документов.",
            "MCP и инструменты: проектирование tool-слоя, MCP-интеграций и контрактов между агентом, внешними сервисами и пользовательским интерфейсом.",
            "Надёжность: Linux, Docker, nginx, CI/CD, логи, smoke/UI-проверки, наблюдаемость, диагностика инцидентов, безопасный деплой и откат.",
            "Коммуникация: архитектурная документация, декомпозиция неясных требований, согласование решений с заказчиком и передача технического контекста команде.",
        ],
        "experience_t": "Проектный опыт - 3 года 2 месяца",
        "projects_page1": [
            (
                "AI-ассистенты и автоматизация рабочих процессов",
                "AI / Backend Engineer",
                [
                    "Проектирование диалоговых ассистентов для web-, Telegram- и внутренних сценариев с подключением API, документов, форм, уведомлений и бизнес-логики.",
                    "Реализация tool/function calling, маршрутизации запросов, управления контекстом, шаблонов промптов и структурированных ответов.",
                    "Разработка backend-компонентов на Python, интеграция с LLM API, базами данных и внешними сервисами; обработка ошибок и контролируемые fallback-сценарии.",
                    "Проверка качества через тестовые наборы и пользовательские сценарии, версионирование изменений, логирование и анализ нестабильных ответов.",
                ],
            ),
            (
                "Геопространственная платформа и пакетный геокодер",
                "Backend / Data / AI Engineer",
                [
                    "Разработка операционной веб-платформы, объединяющей доменные записи, карту, поиск, валидацию и backend-процессы для анализа и координации.",
                    "Пайплайн обработки XLSX/XLS/CSV: автоматическое определение адресных колонок, нормализация, пакетная обработка, оценка уверенности и сценарии ручной проверки.",
                    "Работа с большими выгрузками, проверкой качества результатов и безопасным развёртыванием отдельного сервиса в существующем production-контуре.",
                    "Linux/Docker/nginx, логи, smoke- и UI-проверки, диагностика проблем данных и инфраструктуры без нарушения работы основного продукта.",
                ],
            ),
        ],
        "experience_cont_t": "Проектный опыт - продолжение",
        "projects_page2": [
            (
                "Paragon - терминальное AI-ядро и агентная архитектура",
                "Автор проекта / Rust Engineer",
                [
                    "Спроектировал архитектуру модульного terminal-first AI-ядра для облачных и локальных моделей, нативных coding-агентов и подключаемых инструментов.",
                    "Подготовил компилируемый Rust workspace scaffold с границами provider-, agent-, Git-, storage-, TUI- и module-подсистем.",
                    "Заложил модель разрешений tools, журнал событий сессии, pause/resume/interrupt, видимость Git diff и слои MCP/custom profiles/sandbox/approvals.",
                    "Документировал архитектурные решения, контракты модулей, риски и очередь реализации; проект находится в стадии последовательной разработки.",
                ],
            ),
            (
                "Backend-сервисы и внутренние инструменты",
                "Backend Engineer",
                [
                    "REST API, сервисные компоненты, PostgreSQL/Redis, фоновые задачи, обработка файлов, административные утилиты и отчётные потоки.",
                    "Автоматизация повторяющихся операций и интеграция разрозненных инструментов в воспроизводимые процессы с понятными логами и состояниями.",
                    "Поддержка полного пользовательского сценария: от требований и схемы данных до деплоя, проверки и восстановления после сбоев.",
                ],
            ),
        ],
        "tech_t": "Технологии",
        "tech": [
            "Основной стек: Python, FastAPI, SQL, PostgreSQL, Redis, REST API, Linux, Docker, nginx, Git, CI/CD, Bash.",
            "AI / LLM: LLM API, prompt engineering, structured output, function/tool calling, RAG, embeddings, agents, memory/context, MCP, Ollama, локальный inference.",
            "Дополнительно: Java, Rust, обработка таблиц и документов, геопространственные системы, data validation, observability, архитектурная документация.",
        ],
        "education_t": "Образование",
        "education": "Дальневосточный федеральный университет (ДВФУ), Институт математики и компьютерных технологий - высшее образование, обучаюсь.",
        "extra_t": "Дополнительная информация",
        "extra": [
            "Открытый профиль и проекты: github.com/renosaza; техническое портфолио: renosaza.github.io.",
            "Предпочитаю задачи, где LLM является частью измеримого продукта: ассистенты, автоматизация, поиск по знаниям, обработка документов и внутренние платформы.",
            "Не ограничиваюсь промптами: рассматриваю данные, backend, интеграции, безопасность, деплой и наблюдаемость как единый контур системы.",
        ],
        "footer": "Лапошин Владислав - AI / LLM-инженер",
    }


def page_decor(canvas, doc, footer_text):
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 14 * mm, width - doc.rightMargin, 14 * mm)
    canvas.setFont("ResumeSans", 7.4)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 9 * mm, footer_text)
    canvas.drawRightString(width - doc.rightMargin, 9 * mm, str(doc.page))
    canvas.restoreState()


def build(path, lang):
    d = data(lang)
    styles = styles_for()
    doc = SimpleDocTemplate(
        str(path), pagesize=A4, rightMargin=17 * mm, leftMargin=17 * mm,
        topMargin=14 * mm, bottomMargin=19 * mm,
        title=f"{d['name']} - {d['role']}", author=d["name"],
        subject="Official AI / LLM engineer resume",
    )

    story = [
        p(escape(d["name"]), styles["name"]),
        p(escape(d["role"]), styles["role"]),
        p(escape(d["contact"]), styles["contact"]),
        p(escape(d["meta"]), styles["summary_meta"]),
    ]
    story += section(d["profile_t"], styles)
    story.append(p(escape(d["profile"]), styles["body"]))
    story += section(d["skills_t"], styles)
    story.extend(bullet(item, styles) for item in d["skills"])
    story += section(d["experience_t"], styles)
    for title, role, bullets in d["projects_page1"]:
        story.append(role_block(title, role, bullets, styles))

    story.append(PageBreak())
    story += section(d["experience_cont_t"], styles)
    for title, role, bullets in d["projects_page2"]:
        story.append(role_block(title, role, bullets, styles))
    story += section(d["tech_t"], styles)
    story.extend(bullet(item, styles) for item in d["tech"])
    story += section(d["education_t"], styles)
    story.append(p(escape(d["education"]), styles["body"]))
    story += section(d["extra_t"], styles)
    story.extend(bullet(item, styles) for item in d["extra"])

    doc.build(
        story,
        onFirstPage=lambda c, doc_: page_decor(c, doc_, d["footer"]),
        onLaterPages=lambda c, doc_: page_decor(c, doc_, d["footer"]),
    )


if __name__ == "__main__":
    build(ROOT / "renosaza_resume.pdf", "en")
    build(ROOT / "renosaza_resume_ru.pdf", "ru")
