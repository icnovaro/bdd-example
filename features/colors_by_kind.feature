Feature: Gets colors by kind
  As an user,
  I want to get colors by kind
  So that they can be used in my paintings

Scenario Outline: Request colors url
    Given colors url
    When colors are requested by kind: <kind>
    Then response status code is 200
    And colors must be <colors>

  Examples: Kinds
     | kind          | colors                    |
     | primary       | yellow,blue,red           |
     | secondary     | green,violet,orange       |
     | tertiary      | orange-yellow,red-orange  |