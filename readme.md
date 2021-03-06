# Install pip3

$ sudo apt-get install python3-pip

# Install all required files

$ pip3 install -r requirements.txt

# Run tests

$ behave ./features

# Run with allure report

$ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

# Open allure report

$ allure serve %allure_result_folder%

# Success overview screen

![Alt text](./readme_screenshots/Success_Overview.png?raw=true "Title")

# Succes suites screen

![Alt text](./readme_screenshots/Success_Suites.png?raw=true "Title")

# Failed scenario with the screenshot

![Alt text](./readme_screenshots/Errors.png?raw=true "Title")