
### Step 1. Environment configuration

a) Execute the following commands as a pre-requisite

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`mkdir features`

`mkdir features/steps`

a) Create .feature file

`touch search_in_duckduckgo.feature`

b) Add feature description in `.feature` file

```
Feature: Search content in duckduckgo
  As an user,
  I want to get answers for search terms via a REST API,
  So that my app can get answers anywhere.
```

### Step 2. Write the scenery(s)

a) Write scenery's description in `.feature` 

```
Scenario: Basic DuckDuckGo API Search
    Given a duckduckgo API endpoint
    When the DuckDuckGo API is queried with hello world
    Then the response status code is 200
    And the response contains results for hello world
```

b) Create .py file with same name as .feature in `features/steps` folder

`touch features/steps/search_in_duckduckgo.py`

c) Now exec behave command in your terminal

`behave`

now, you should see a message like this one:

```
You can implement step definitions for undefined steps with these snippets:

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
```

d) then copy and paste the content of @given @when @then to feature/steps/search_in_duckduckgo.py file

### Step 3. Implement steps

