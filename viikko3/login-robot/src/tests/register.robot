*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    matti    matti123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials    kalle    kalle123
    Output Should Contain    User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    ma    matti123
    Output Should Contain    Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials    matti    asd
    Output Should Contain    Password must be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    matti    mattikatti
    Output Should Contain    Password can not only consist of letters a-z