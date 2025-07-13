from dotenv import load_dotenv
import os
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.tavily_search import TavilySearchResults
import yfinance as yf
from models.models import ToolsdataModel
import traceback
from langchain.globals import set_verbose
set_verbose(True)

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


@tool
def latest_news_based_on_query(arg)-> str:
    """
    Based on user query, this will search the data in DuckDuckGoSearchRun for get the latest news related
    :param query:
    :return:
    """
    try:
        # search_tool = DuckDuckGoSearchRun()
        search_tool = TavilySearchResults()
        response = search_tool.invoke(arg)
        print("----------------Tavily Search Result -------------")
        print(response)
        return {"messages": response}
    except Exception:
        traceback.print_exc()


@tool
def get_the_stock_price_of_ticker(state: ToolsdataModel) -> float:
    """
    get a stock price from yahoo finance
    :param ticker:
    :return:
    """
    stock = yf.Ticker(state['query'])
    return stock.info['previousClose']