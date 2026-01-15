# Agentic Notebook-LM (CrewAI)

An advanced multi-agent system designed to mimic the functionality of Google's **NotebookLM**. This application ingests heterogeneous data sources—including YouTube videos, web articles, arXiv research papers, and local documents—to synthesize them into a structured, beginner-friendly Markdown guide.

***

## 🚀 Overview

The system utilizes **CrewAI Flows** to orchestrate two distinct agent crews through a state-managed pipeline:

- **Research Crew (Hierarchical)**: A manager-led team that extracts and synthesizes raw data from various URLs and files.  
- **Writer Crew (Sequential)**: A linear pipeline that transforms dense research into a polished, educational “Getting Started” guide.

***

## 🏗️ Architecture Flow

The application logic is divided into three primary phases managed by a **Pydantic-based state**:

1. **Phase 1: Research Node**  
   Triggered by raw user inputs. The Research Manager analyzes the URLs and delegates tasks to specialists (YouTube, Web, Arxiv, or Document).

2. **Phase 2: Transition**  
   Compiled research data (minimum 5000 words) is passed to the Writing state.

3. **Phase 3: Writing Node**  
   The Technical Writer drafts the guide, and the Content Editor performs a final quality assurance check.

***

## 🤖 The Crews

### 1. Research Crew (Hierarchical Process)

Coordinated by a Research Manager who ensures thorough coverage without losing technical details.

- **YouTube Specialist**: Uses `YoutubeVideoSearchTool` and `YoutubeChannelSearchTool` to analyze transcripts.  
- **Web Specialist**: Employs `ScrapeWebsiteTool` and `SeleniumScrapingTool` for static and dynamic web content.  
- **Arxiv Specialist**: Analyzes academic papers using `ArxivPaperTool`.  
- **Document Specialist**: Processes PDFs, text, and Markdown files using semantic search.

### 2. Writer Crew (Sequential Process)

Transforms complex findings into an accessible and structured format.

- **Technical Writer**: Focuses on beginner-friendly language, analogies, and line-by-line code explanations.  
- **Content Editor**: Reviews the guide for clarity, technical accuracy, and tone consistency.

***

## 🛠️ Technical Setup

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

Activate the environment:

```bash
source .venv/bin/activate
```

***

## 💻 Usage

Run the flow via the interactive terminal interface:

```bash
python src/guide_generator_flow/main.py
```

You will be prompted to provide optional links for:

- YouTube videos or channels  
- Web articles or documentation  
- arXiv paper IDs or titles  
- Local file paths (PDF/TXT/MD)

The final output will be saved as:

```text
./outputs/getting_started_guide.md
```

***

## 📂 File Structure

- `src/guide_generator_flow/crews/research_crew/`: Configs and logic for the Research phase.  
- `src/guide_generator_flow/crews/writing_crew/`: Configs and logic for the Writing phase.  
- `src/guide_generator_flow/main.py`: CrewAI Flow orchestration and state management.

***
