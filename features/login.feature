Feature: Login

Scenario Outline: user should login with valid credentials and should not login with invalid credentials
    Given I have opened login page
      When I login with "<username>" name and "<password>" password
      Then I see "<message>" text 

Examples:
    | username | password | message       |
    | admin    | 12345    | WELCOME :)    |
    | admin    | 13232    | ACCESS DENIED!|
    | adin     | 12345    | ACCESS DENIED!|

Scenario Outline: user should login with valid credentials and should not login with invalid credentials through the api
    Given I have opened login page
      When I login through the api with "admin" name and "12345" password
      Then I should get "200" response code   
        And I should get "WELCOME :)" message in the response 

Examples:
    | username | password | message       | code |
    | admin    | 12345    | WELCOME :)    | 200  |
    | admin    | 13232    | ACCESS DENIED!| 200  |
    | adin     | 12345    | ACCESS DENIED!| 200  |

Scenario: user should not be logged without properly stored cookie
    Given I have opened login page
      When I login with "admin" name and "12345" password
        And I refresh cookie
      Then I see "THE SESSION COOKIE IS MISSING OR HAS A WRONG VALUE!" text       
