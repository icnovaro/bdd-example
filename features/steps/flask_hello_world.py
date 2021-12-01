import requests

from behave import *

@given(u'a local server url')
def step_impl(context):
    context.api_url = 'http://localhost:5000/'


@when(u'the hello world endpoint is requested')
def step_impl(context):
    context.response = requests.get(f"{context.api_url}/hello")


@then(u'response status code is 200')
def step_impl(context):
    assert context.response.status_code == 200

@then(u'response message must be hello world')
def step_impl(context):
    assert context.response.text == 'Hello, World!'