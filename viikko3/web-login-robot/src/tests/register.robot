*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application and Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  aapo
    Set Password  aapo1234
    Set Password Confirmation  aapo1234
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Fail With Message  Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  ka
    Set Password Confirmation  ka
    Submit Register Credentials
    Register Should Fail With Message  Password must be atleast 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  matti321
    Submit Register Credentials
    Register Should Fail With Message  Passwords did not match

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed
    Reset Application

Login After Failed Registration
    Set Username  seppo
    Set Password  seppo123
    Set Password Confirmation  matti321
    Submit Register Credentials
    Register Should Fail With Message  Passwords did not match
    Go To Login Page
    Set Username  seppo
    Set Password  seppo123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application and Go To Register Page
    Reset Application
    Go To Register Page