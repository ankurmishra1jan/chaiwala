import pandas as pd
from typing import Literal
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
import yfinance as yf
from models.models import ToolsdataModel


@tool
def latest_news_based_on_query(state: ToolsdataModel)-> str:
    """
    Based on user query, this will search the data in YahooFinanceNews for get the latest news related stock
    :param ticker_name:
    :return:
    """
    search_tool = DuckDuckGoSearchRun()
    return search_tool.invoke(state['query'])


@tool
def get_the_stock_price_of_ticker(state: ToolsdataModel) -> float:
    """
    get a stock price from yahoo finance
    :param ticker:
    :return:
    """
    stock = yf.Ticker(state['query'])
    return stock.info['previousClose']