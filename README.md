
# Agentic Notebook-LM (CrewAI)
An advanced multi-agent system designed to mimic the functionality of Google's NotebookLM11. This application ingests heterogeneous data sources—including YouTube videos, web articles, arXiv research papers, and local documents—to synthesize them into a structured, beginner-friendly Markdown guide2222.
+1

🚀 Overview
The system utilizes CrewAI Flows to orchestrate two distinct crews through a state-managed pipeline3:

Research Crew (Hierarchical): A manager-led team that extracts and synthesizes raw data from various URLs and files4444.
+2

Writer Crew (Sequential): A linear pipeline that transforms dense research into a polished, educational "Getting Started" guide5555.
+3

🏗️ Architecture Flow
The application logic is divided into three primary phases managed by a Pydantic-based state666:
+1

Phase 1: Research Node: Triggered by raw user inputs. The Research Manager analyzes the URLs and delegates tasks to specialists (YouTube, Web, Arxiv, or Document)7777.
+1

Phase 2: Transition: Compiled research data (minimum 5000 words) is passed to the Writing state8888.
+1

Phase 3: Writing Node: The Technical Writer drafts the guide, and the Content Editor performs a final quality assurance check9999.
+1

🤖 The Crews

1. Research Crew (Hierarchical Process)
Coordinated by a Research Manager who ensures thorough coverage without losing technical details10.

YouTube Specialist: Uses YoutubeVideoSearchTool and YoutubeChannelSearchTool to analyze transcripts111111.
+1

Web Specialist: Employs ScrapeWebsiteTool and SeleniumScrapingTool for static and dynamic web content12121212.
+1

Arxiv Specialist: Analyzes academic papers using ArxivPaperTool1313131313.
+3

Document Specialist: Processes PDFs, Text, and Markdown files using semantic search141414141414141414.
+2

2. Writer Crew (Sequential Process)
Transforms complex findings into an accessible format15151515.
+1

Technical Writer: Focuses on beginner-friendly language, analogies, and line-by-line code explanations16161616.
+1

Content Editor: Reviews the guide for clarity, technical accuracy, and tone consistency17171717.
+1

🛠️ Technical Setup
Prerequisites
Python 3.10+
[CrewAI](https://crewai.com)
An OpenAI API Key (configured as manager_llm) 18

Installation
Clone the repository:
Bash
git clone [https://github.com/your-username/agentic-notebook-lm.git](https://github.com/your-username/agentic-notebook-lm.git)
cd agentic-notebook-lm

Install dependencies:
Using uv as specified in the project19:
Bash
crewai install
uv add selenium webdriver-manager

Activate environment:
Bash
source .venv/bin/activate

💻 Usage
Run the flow via the interactive terminal interface20:

Bash
python src/guide_generator_flow/main.py

You will be prompted to provide optional links for21:

YouTube Videos/Channels
Web Articles/Documentation
arXiv Paper IDs or Titles
Local file paths (PDF/TXT/MD)
The final output will be saved as ./outputs/getting_started_guide.md22.

📂 File Structure

src/guide_generator_flow/crews/research_crew/: Configs and logic for the Research phase23.

src/guide_generator_flow/crews/writing_crew/: Configs and logic for the Writing phase24.

src/guide_generator_flow/main.py: The CrewAI Flow orchestration and state management25.

Agentic Notebook-LM (CrewAI)
=============================

An advanced multi-agent system designed to mimic the functionality of Google's NotebookLM. This application ingests heterogeneous data sources—including YouTube videos, web articles, arXiv research papers, and local documents—to synthesize them into a structured, beginner-friendly Markdown guide.

🚀 Overview
-----------

The system utilizes CrewAI Flows to orchestrate two distinct crews through a state-managed pipeline:

- **Research Crew (Hierarchical)**: A manager-led team that extracts and synthesizes raw data from various URLs and files.
- **Writer Crew (Sequential)**: A linear pipeline that transforms dense research into a polished, educational "Getting Started" guide.

🏗️ Architecture Flow
---------------------

The application logic is divided into three primary phases managed by a Pydantic-based state:

- **Phase 1: Research Node**: Triggered by raw user inputs. The Research Manager analyzes the URLs and delegates tasks to specialists (YouTube, Web, Arxiv, or Document).
- **Phase 2: Transition**: Compiled research data (minimum 5000 words) is passed to the Writing state.
- **Phase 3: Writing Node**: The Technical Writer drafts the guide, and the Content Editor performs a final quality assurance check.

🤖 The Crews
------------

### 1. Research Crew (Hierarchical Process)

Coordinated by a Research Manager who ensures thorough coverage without losing technical details.

- **YouTube Specialist**: Uses `YoutubeVideoSearchTool` and `YoutubeChannelSearchTool` to analyze transcripts.
- **Web Specialist**: Employs `ScrapeWebsiteTool` and `SeleniumScrapingTool` for static and dynamic web content.
- **Arxiv Specialist**: Analyzes academic papers using `ArxivPaperTool`.
- **Document Specialist**: Processes PDFs, text, and Markdown files using semantic search.


### 2. Writer Crew (Sequential Process)

Transforms complex findings into an accessible format.

- **Technical Writer**: Focuses on beginner-friendly language, analogies, and line-by-line code explanations.
- **Content Editor**: Reviews the guide for clarity, technical accuracy, and tone consistency.

🛠️ Technical Setup
-------------------

### Prerequisites

- Python 3.10+
- [CrewAI](https://crewai.com)
- An OpenAI API Key (configured as `manager_llm`)


### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/agentic-notebook-lm.git
cd agentic-notebook-lm
```

Install dependencies (using `uv` as specified in the project):

```bash
crewai install
uv add selenium webdriver-manager
```

Activate environment:

```bash
source .venv/bin/activate
```

💻 Usage
--------

Run the flow via the interactive terminal interface:

```bash
python src/guide_generator_flow/main.py
```

You will be prompted to provide optional links for:

- YouTube videos/channels
- Web articles/documentation
- arXiv paper IDs or titles
- Local file paths (PDF/TXT/MD)

The final output will be saved as:

```text
./outputs/getting_started_guide.md
```

📂 File Structure
-----------------

- `src/guide_generator_flow/crews/research_crew/`: Configs and logic for the Research phase.
- `src/guide_generator_flow/crews/writing_crew/`: Configs and logic for the Writing phase.
- `src/guide_generator_flow/main.py`: The CrewAI Flow orchestration and state management.

