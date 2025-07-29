import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/investing-cryptocurrency-markets'

mcp = FastMCP('investing-cryptocurrency-markets')

@mcp.tool()
def get_meta_data(locale_info: Annotated[str, Field(description='The language code')],
                  lang_ID: Annotated[Union[int, float, None], Field(description='The value of all_langs/lang_ID returned in .../get-meta-data endpoint Default: 1')] = None,
                  time_utc_offset: Annotated[Union[int, float, None], Field(description='UTC value in seconds, for example : utc+8 -> 8 * 60 * 60 = 28800 Default: 28800')] = None) -> dict: 
    '''Get init meta data'''
    url = 'https://investing-cryptocurrency-markets.p.rapidapi.com/get-meta-data'
    headers = {'x-rapidapi-host': 'investing-cryptocurrency-markets.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'locale_info': locale_info,
        'lang_ID': lang_ID,
        'time_utc_offset': time_utc_offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_ico_calendar(tabname: Annotated[Union[str, None], Field(description='One of the following : upcoming|completed|ongoing')] = None,
                     lang_ID: Annotated[Union[int, float, None], Field(description='The value of all_langs/lang_ID returned in .../get-meta-data endpoint Default: 1')] = None,
                     time_utc_offset: Annotated[Union[int, float, None], Field(description='UTC value in seconds, for example : utc+8 -> 8 * 60 * 60 = 28800 Default: 28800')] = None,
                     category: Annotated[Union[str, None], Field(description='Check for suitable value of icoData/categories returned right in this endpoint. Separated by comma for multiple options. For example : _ico_cat_gaming,_ico_cat_ecomm,_ico_cat_finance,_ico_cat_healthcare')] = None,
                     sort: Annotated[Union[str, None], Field(description='One of the following is allowed related_days | name | funds_raised | completed')] = None) -> dict: 
    '''Get ICO calendar'''
    url = 'https://investing-cryptocurrency-markets.p.rapidapi.com/get-ico-calendar'
    headers = {'x-rapidapi-host': 'investing-cryptocurrency-markets.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tabname': tabname,
        'lang_ID': lang_ID,
        'time_utc_offset': time_utc_offset,
        'category': category,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def currencies_list(lang_ID: Annotated[Union[int, float, None], Field(description='The value of all_langs/lang_ID returned in .../get-meta-data endpoint Default: 1')] = None,
                    time_utc_offset: Annotated[Union[int, float, None], Field(description='UTC value in seconds, for example : utc+8 -> 8 * 60 * 60 = 28800 Default: 28800')] = None) -> dict: 
    '''List all available currencies'''
    url = 'https://investing-cryptocurrency-markets.p.rapidapi.com/currencies/list'
    headers = {'x-rapidapi-host': 'investing-cryptocurrency-markets.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lang_ID': lang_ID,
        'time_utc_offset': time_utc_offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def currencies_get_rate(fromCurrency: Annotated[Union[int, float], Field(description='Value of currency_ID field returned in currencies/list endpoint Default: 189')],
                        toCurrency: Annotated[Union[int, float], Field(description='Value of currency_ID field returned in currencies/list endpoint Default: 12')],
                        lang_ID: Annotated[Union[int, float, None], Field(description='The value of all_langs/lang_ID returned in .../get-meta-data endpoint Default: 1')] = None,
                        time_utc_offset: Annotated[Union[int, float, None], Field(description='UTC value in seconds, for example : utc+8 -> 8 * 60 * 60 = 28800 Default: 28800')] = None) -> dict: 
    '''Get exchange rate between two different currencies'''
    url = 'https://investing-cryptocurrency-markets.p.rapidapi.com/currencies/get-rate'
    headers = {'x-rapidapi-host': 'investing-cryptocurrency-markets.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fromCurrency': fromCurrency,
        'toCurrency': toCurrency,
        'lang_ID': lang_ID,
        'time_utc_offset': time_utc_offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
