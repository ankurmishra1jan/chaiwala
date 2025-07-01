import pandas as pd
from typing import Literal
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool


@tool
def latest_news_based_on_ticker():
    pass


@tool
def ticker_name_based_on_query():
    pass