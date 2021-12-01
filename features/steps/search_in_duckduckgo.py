import requests

from behave import *

@given(u'a duckduckgo API endpoint')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a duckduckgo API endpoint')


@when(u'the DuckDuckGo API is queried with hello world')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the DuckDuckGo API is queried with hello world')


@then(u'the response status code is 200')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response status code is 200')


@then(u'the response contains results for hello world')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response contains results for hello world')