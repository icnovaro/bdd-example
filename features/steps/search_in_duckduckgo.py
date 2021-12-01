import requests

from behave import *

@given(u'a duckduckgo API endpoint')
def step_impl(context):
    context.api_url = 'https://api.duckduckgo.com/'

@when(u'the DuckDuckGo API is queried with hello world')
def step_impl(context):
    params = {'q': 'hello world', 'format': 'json'}
    context.response = requests.get(context.api_url, params=params)

@then(u'the response status code is 200')
def step_impl(context):
    assert context.response.status_code == 200

@then(u'the response contains results for hello world')
def step_impl(context):
    json_data = context.response.json()["Heading"]
    assert json_data == "Hello World"