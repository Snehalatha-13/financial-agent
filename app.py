import os
from dotenv import load_dotenv
from phi.assistant import Assistant
from phi.llm.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


load_dotenv() 

# Web Search Assistant
web_search_assistant = Assistant(
    name="WebSearchAgent",
    role="You are a top-tier web search agent. Your primary goal is to find the most relevant and up-to-date information from the internet.",
    llm=Groq(model="llama3-8b-8192"),
    tools=[DuckDuckGo()],
    instructions=["You must always include the source URL for the information you provide."],
    show_tool_calls=True,
    markdown=True,
)
# Financial Assistant
finance_assistant = Assistant(
    name="FinanceAgent",
    role="You are a world-class financial analyst. You provide accurate stock data and analysis.",
    llm=Groq(model="llama3-8b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display financial data like analyst recommendations for clarity."],
    show_tool_calls=True,
    markdown=True,
)
# Multi Agent 
multi_agent_manager = Assistant(
    name="ChiefAnalyst",
    team=[web_search_assistant, finance_assistant],
    llm=Groq(model="llama3-70b-8192"),
    instructions=[
        "Delegate tasks to the appropriate agent in your team.",
        "Use the FinanceAgent for stock-specific data like recommendations.",
        "Use the WebSearchAgent for recent news and articles.",
        "Synthesize the information from your team into a single, comprehensive response.",
        "Always include sources for news and present financial data in tables."
    ],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    multi_agent_manager.print_response(
        "Summarize analyst recommendations and share the latest news for Adani Enterprises", 
        stream=True
    )