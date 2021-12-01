Feature: Trigger hello world endpoint
  As an user,
  I want to trigger the hello world enpoint of local flask,
  So that can test the server locally

Scenario: Request hellowold endpoint
    Given a local server url
    When the hello world endpoint is requested
    Then response status code is 200
    And response message must be hello world