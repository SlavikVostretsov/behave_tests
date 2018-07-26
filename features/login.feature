Feature: Login

Background:
    Given I have opened login page


Scenario: user should login with valid credentials
    When I login with "admin" name and "12345" password
    Then I see "WELCOME :)" text 


Scenario Outline: user should not login with invalid credentials
    When I login with "<username>" name and "<password>" password
    Then I see "ACCESS DENIED!" text 

Examples:
    | username | password |
    | admin    | 13232    |
    | adin     | 12345    | 


Scenario: user should login with valid credentials through the http request
    When I login through the http with "admin" name and "12345" password
    Then I should get "200" response code   
        And I should get "WELCOME :)" message in the response 


Scenario Outline: user should not login with invalid credentials through the http request
    When I login through the http with "<username>" name and "<password>" password
    Then I should get "200" response code   
        And I should get "ACCESS DENIED!" message in the response 

Examples:
    | username | password |
    | admin    | 13232    |
    | adin     | 12345    |


Scenario: user should not be logged without properly stored cookie
    When I login with "admin" name and "12345" password
        And I refresh cookie
    Then I see "THE SESSION COOKIE IS MISSING OR HAS A WRONG VALUE!" text       
