*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page



*** Test Cases ***

Register With Valid Username And Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  asdasdasasas
    Set Password  salasana123456
    Set Confirmation  salasana123456
    Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  a
    Set Password  salasana123456
    Set Confirmation  salasana123456   
    Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  asdasdasdasd
    Set Password  sa256
    Set Confirmation  sa256
    Register
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  testikayttaja
    Set Password  saasasa256
    Set Confirmation  sasasaas253442
    Register
    Register Should Fail With Message  Wrong confirmation password

Login After Successful Registration
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  testattud
    Set Password  salasana123456
    Set Confirmation  salasana123456
    Register
    Welcome Page Should Be Open

    Go To Main Page
    Go To Login Page
    Set Username  testattud
    Set Password  salasana123456
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Click Link  Register new user
    Register Page Should Be Open
    Set Username  a
    Set Password  salasana123456
    Set Confirmation  salasana123456   
    Register
    Register Should Fail With Message  Username too short

    Go To Main Page
    Go To Login Page
    Set Username  a
    Set Password  salasana123456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password  
    



*** Keywords ***
Register
    Click Button  Register

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
