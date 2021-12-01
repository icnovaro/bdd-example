Feature: Buscar contenido en duckduckgo
  As an user,
  I want to get answers for search terms via a REST API,
  So that my app can get answers anywhere.

Scenario: Basic DuckDuckGo API Search
    Given a duckduckgo API endpoint
    When the DuckDuckGo API is queried with hello world
    Then the response status code is 200
    And the response contains results for hello world

