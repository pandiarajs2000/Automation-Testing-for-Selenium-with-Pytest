from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class CustomerDetails:
    def __init__(self, driver):
        self.driver = driver
        self.fname_xpath = (By.XPATH, "//input[@id='firstname']")
        self.lname_xpath = (By.XPATH, "//input[@id='lastname']")
        self.gstin_xpath = (By.XPATH,"//input[@id = 'gstin']")
        self.email_xpath = (By.XPATH, "//input[@id = 'email']")
        self.phone_xpath = (By.XPATH, "//input[@id = 'phone']")
        self.p_date = (By.XPATH, "//input[@id = 'dob']")
        self.time_xpath = (By.ID, "//input[@id = 'posting_time']")
        self.message = (By.TAG_NAME,"p")
        self.btn = (By.TAG_NAME, "button"   )
    
    def site_url(self):
        url = self.driver.get('http://127.0.0.1:5000/master_screen')
        time.sleep(5)
        return url
    def submit_form(self, first_name, last_name, gstin, email, phone):
        self.driver.implicitly_wait(20)
        # insert the values
        self.driver.find_element(*self.fname_xpath).send_keys(first_name)
        self.driver.find_element(*self.lname_xpath).send_keys(last_name)
        self.driver.find_element(*self.gstin_xpath).send_keys(gstin)
        self.driver.find_element(*self.email_xpath).send_keys(email)
        self.driver.find_element(*self.phone_xpath).send_keys(phone)
        self.driver.find_element(*self.btn).click()
        time.sleep(20)
        response = self.get_message()
        time.sleep(10)
        return response
    
    def check_customer_first_name(self, first_name=None):
        if first_name is not None:
            self.driver.find_element(*self.fname_xpath).send_keys(first_name)
            self.driver.find_element(*self.btn).click()
            message = self.get_message()
            return message
        
    def check_customer_last_name(self, last_name=None, first_name=None):
        if last_name and first_name is not None:
            self.driver.find_element(*self.fname_xpath).send_keys(first_name)
            self.driver.find_element(*self.lname_xpath).send_keys(last_name)
            self.driver.find_element(*self.btn).click()
            time.sleep(3)
            message = self.get_message()
            return message
    
    def check_customer_gstin_number(self, gstin=None, firstname=None):
        if gstin and firstname is not None:
            self.driver.find_element(*self.fname_xpath).send_keys(firstname)
            self.driver.find_element(*self.gstin_xpath).send_keys(gstin)
            self.driver.find_element(*self.btn).click()
            message = self.get_message()
            return message

    def email_validation(self, first_name, last_name, gstin, email, phone):
        self.driver.implicitly_wait(20)
        # insert the values
        self.driver.find_element(*self.fname_xpath).send_keys(first_name)
        self.driver.find_element(*self.lname_xpath).send_keys(last_name)
        self.driver.find_element(*self.gstin_xpath).send_keys(gstin)
        # email = self.driver.find_element(*self.email_xpath).send_keys(email)
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_xpath))
        email_input.send_keys(email)
        message = self.driver.execute_script("return arguments[0].validationMessage;", email_input)
        time.sleep(10)
        return message

    def get_popup_message(self):
        alert_msg = self.driver.switch_to.alert
        response = alert_msg.text
        alert_msg.accept()
        return response

    def get_message(self):
        time.sleep(3)
        result = self.driver.find_element(*self.message).text
        return result