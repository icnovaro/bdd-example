import requests
import json
from behave import *

@given(u'colors url')
def step_impl(context):
    context.api_url = 'http://localhost:5000/colors'

@when(u'colors are requested by kind: {kind}')
def step_impl(context, kind):
    context.response = requests.get(f"{context.api_url}?kind={kind}")

# important! You can't define existing step, they are reusable
# @then(u'response status code is 200')
# def step_impl(context):
#     assert context.response.status_code == 200

@then(u'colors must be {colors}')
def step_impl(context, colors):
    data = json.loads(context.response.text)
    data_colors = data.get("colors")
    formated_colors = colors.split(',')
    
    for i, j in zip(formated_colors, data_colors):
        assert i == j