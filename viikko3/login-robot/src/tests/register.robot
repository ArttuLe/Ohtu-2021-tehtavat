*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  asdddd  asddd2134512
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle12341232132
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle321321321
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  kayttaja  kall123
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kayttaja  kalllasdlsadsal
    Output Should Contain  Password must contain numbers and letters


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle1233123213
    Input Register Command