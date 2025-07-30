# Agentic-AI Financial Analysis Tool

This repository contains the code for building an end-to-end agentic AI application for financial analysis. This tool utilizes the **Phi data** framework to create and manage a multi-agent system capable of providing comprehensive financial information.

## Overview

The core of this project is a "Financial Agent" application composed of two independent agents:

* **Web Search Agent:** This agent leverages the DuckDuckGo Search tool to find relevant information on the web. It's designed to always include sources for its findings.
* **Financial Agent:** This agent uses the `yfinance` library to fetch detailed stock information, including analyst recommendations, fundamental data, and company news.

These two agents work in tandem within a `multi_agent` workflow to answer complex queries about financial instruments. For example, you can ask for a summary of analyst recommendations and the latest news for a specific stock, and the agents will collaborate to provide a comprehensive response.

## Features

* **Multi-Agent System:** Combines the strengths of a web search agent and a financial data agent to provide rich, detailed information.
* **LLM Integration:** Utilizes the **Grok** large language model for natural language understanding and generation. The framework is flexible and supports other LLMs as well.
* **Interactive Playground:** Integrates with Phi data's playground for an easy-to-use, conversational interface to interact with the financial analysis agent.
* **Extensible:** The framework is open-source and allows for the integration of various other tools and services.

## Getting Started

### Prerequisites

* Python 3.x
* A virtual environment manager (e.g., `venv`)
* API keys for **Grok** and **Phi data**

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Snehalatha-13/financial-agent.git](https://github.com/Snehalatha-13/financial-agent.git)
    cd financial-agent
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    Assuming a `requirements.txt` file exists:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: Based on the video, you would need to install `phidata`, `python-dotenv`, `yfinance`, `duckduckgo-search`, `fastapi`, `uvicorn`, and `groq`.*

4.  **Configure your API keys:**
    Create a `.env` file in the root of the project and add your API keys:
    ```
    GROK_API_KEY="YOUR_GROK_API_KEY"
    PHIDATA_API_KEY="YOUR_PHIDATA_API_KEY"
    ```

## Usage

To run the application, you can either use the interactive playground provided by Phi data or run the application directly.

### Interactive Playground

1.  Launch the Phi data playground.
2.  Load the agent configuration from the repository.
3.  Start a conversation with the "Financial Agent." You can ask questions like:
    * "What are the latest analyst recommendations for NVDA?"
    * "Summarize the recent news for Tesla."

### Direct Execution

You can also run the main Python script to interact with the agent from the command line.

```bash
python main.py
