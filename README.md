# AI Paper Review Agentic

An end-to-end multi-agent AI system that automates academic literature reviews using Large Language Models and the arXiv API.

The application transforms a natural language research topic into a structured literature review by coordinating multiple specialized AI agents. Each agent is responsible for a specific stage of the pipeline, from query generation to producing a final research report.

The project combines LLM reasoning, public scientific APIs, and a lightweight Streamlit interface to demonstrate how agentic workflows can automate complex knowledge-intensive tasks.

---

## Features

- Natural language research topic input
- Automatic generation of optimized arXiv search queries
- Retrieval of the most relevant scientific papers
- AI-powered paper analysis
- Independent AI review of generated analyses
- Automatic synthesis into a final research report
- Interactive Streamlit application
- Modular multi-agent architecture

---

## Agent Workflow

The system is composed of five specialized agents:

### 1. Query Builder Agent

Receives a research topic written in natural language and generates an optimized arXiv query using the official search syntax.

Output:

- optimized search query
- extracted keywords

---

### 2. Search Agent

Uses the generated query to retrieve papers from the arXiv API.

Extracted information includes:

- title
- authors
- publication date
- abstract
- URL

---

### 3. Analyst Agent

Analyzes every retrieved paper individually.

For each paper it generates:

- summary
- main research problem
- main contribution
- applications
- limitations
- relevance score
- relevance explanation

---

### 4. Reviewer Agent

Acts as an independent quality assurance agent.

It validates whether the Analyst's conclusions are supported by the original abstract and produces:

- approval status
- review comments
- unsupported claims
- corrected relevance score
- final relevance explanation

---

### 5. Editor Agent

Synthesizes all approved papers into a final literature review.

The generated report contains:

- executive summary
- research trends
- key differences between papers
- recommended reading order
- final recommendations

---

## Architecture

```
User

↓

Query Builder Agent

↓

Search Agent

↓

Analyst Agent

↓

Reviewer Agent

↓

Editor Agent

↓

Final Research Report
```

---

## Technologies

- Python
- Streamlit
- Groq API
- Llama 3.1
- arXiv API
- Pandas
- Requests
- Jupyter Notebook
- PyArrow

---

## Project Structure

```
ai-paper-review-agentic/

│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── config/
│   ├── input/
│   └── output/
│
├── notebooks/
│   ├── 00_query_builder_agent.ipynb
│   ├── 01_search_agent.ipynb
│   ├── 02_analyst_agent.ipynb
│   ├── 03_reviewer_agent.ipynb
│   └── 04_editor_agent.ipynb
│
└── src/
    └── workflow.py
```

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/your_username/ai-paper-review-agentic.git

cd ai-paper-review-agentic
```

Create the virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
```

Launch the application:

```bash
streamlit run app.py
```

---

## Example

**Input**

```
Multi-agent AI systems for supply chain optimization
```

↓

The application automatically:

- builds an optimized arXiv query
- retrieves relevant papers
- analyzes each publication
- validates the analyses
- generates a final literature review

---

## Future Improvements

- Semantic search using embeddings
- Retrieval-Augmented Generation (RAG)
- PDF parsing and full-text analysis
- Citation graph analysis
- Multi-provider LLM support (OpenAI, Anthropic, Gemini)
- Parallel execution of independent agents
- Automatic report export to PDF and Markdown
- Interactive visualization of paper relationships

---

## License

MIT License
