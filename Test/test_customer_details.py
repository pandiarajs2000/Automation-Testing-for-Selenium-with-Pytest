import selenium
import time
import pytest
import allure
from utils.utils import read_data, write_data, row_count, read_all_data
import logging
from Pages.customer_details_screen import CustomerDetails
# from utils.log_utils import get_logger

# logger = get_logger(__name__)

file_path = "E:\\Frappe Model Project\\Data\\Frappe_Model_QA_Data.xlsx"
rows = row_count(file_path, 'Customer Data')

# @allure.title("Test Customer Master Screen")
# @allure.description("To add the data for the respective field in the customer master screen")
# @allure.severity(allure.severity_level.NORMAL)
# @allure.testcase("TC_001")
# def test_customer_data_add(driver):
#     print("Customer Data Test Scripts")
#     logger.info("This is the customer master screen")
#     form_page = CustomerDetails(driver)
#     form_page.site_url()
#     all_data = read_all_data(file_path, "Customer Data")
#     for data in all_data:
#         print('datas',data[0])
#         form_page.submit_form(data[0], data[1], data[2],data[3],data[4])

@allure.title("Test Customer First Name")
@allure.description("To verify the customer first name should be added for 100 characters or below the 100 characters")
@allure.severity(allure.severity_level.MINOR)
@allure.testcase("TC_001")
@allure.story("Field Validation")
def test_verify_customer_name(driver):
    # logger.info("Customer First Name Field Testing")
    row = 2
    customer_first_name = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"The customer '{customer_first_name}' is added successfully."
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_first_name(customer_first_name)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)

@allure.title("Test Customer First Name")
@allure.description("To verify the customer first name should not be added for greater than 100 characters")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase("TC_002")
@allure.story("Field Validation")
def test_verify_customer_name_long(driver):
    # logger.info("Customer First Name Field Testing")
    row = 3
    customer_first_name = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Data too long for column 'customer_first_name' at row 1"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_first_name(customer_first_name)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)

@allure.title("Test the existing Customer First Name should be added for DB")
@allure.description("To verify the existing customer first name should not be added to the Database.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase("TC_003")
@allure.story("Field Validation")
def test_duplicate_customer_name(driver):
    # logger.info("Customer First Name Field Testing")
    row = 4
    customer_first_name = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"This customer first name already added."
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_first_name(customer_first_name)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To verify the customer last name added without the first name")
@allure.description("To verify the customer last name added without the first name")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase("TC_004")
@allure.story("Customer Lastname Field Validation")
def test_customer_lastname(driver):
    # logger.info("Customer last Name Field Testing")
    row = 5
    customer_last_name = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Please fill the fields firstName field."
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_last_name(customer_last_name)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To verify the customer last name should be five characters or below the five characters")
@allure.description("To verify the customer last name should be five characters or below the five characters")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase("TC_005")
@allure.story("Customer Lastname Field Validation")
@pytest.mark.parametrize("firstname",['Manish'])
def test_last_name_char_limit(driver, firstname):
    # logger.info("Customer last Name Field Testing")
    row = 6
    customer_last_name = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Customer Last name should be below the five characters"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_last_name(customer_last_name,firstname)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To Verify the customer last name should not be special characters")
@allure.description("To Verify the customer last name should not be special characters")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase("TC_005")
@allure.story("Customer Lastname Field Validation")
@pytest.mark.parametrize("firstname",['Manish'])
def test_last_name_char_limit(driver, firstname):
    # logger.info("Customer last Name Field Testing")
    row = 7
    customer_last_name = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Customer Last Name Should Not be Include Special Characters"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_last_name(customer_last_name,firstname)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To verify the valid customer gstin")
@allure.description("To verify the valid customer gstin")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_007")
@allure.story("Customer GSTIN Field Validation")
@pytest.mark.parametrize("firstname",["Krish"])
def test_customer_gstin_valid_data(driver,firstname):
    # logger.info("Customer GSTIN Field Testing")
    row = 8
    customer_gstin = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"The customer '{firstname}' is added successfully."
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_gstin_number(customer_gstin, firstname)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To verify the In-valid customer gstin")
@allure.description("To verify the In-valid customer gstin")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_007")
@allure.story("Customer GSTIN Field Validation")
@pytest.mark.parametrize("firstname",["Krish"])
def test_customer_gstin_invalid_data(driver,firstname):
    # logger.info("Customer GSTIN Field Testing")
    row = 9
    customer_gstin = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Invalid GSTIN Number"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_gstin_number(customer_gstin, firstname)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To Verify the customer gstin number should not be number")
@allure.description("To Verify the customer gstin number should not be number")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_008")
@allure.story("Customer GSTIN Field Validation")
@pytest.mark.parametrize("firstname",["Krish"])
def test_gstin_not_digit(driver,firstname):
    # logger.info("Customer GSTIN Field Testing")
    row = 10
    customer_gstin = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Customer GSTIN Number should not be digits"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_gstin_number(customer_gstin, firstname)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To verify customer gstin number should be 15 characters only")
@allure.description("To verify customer gstin number should be 15 characters only")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_009")
@allure.story("Customer GSTIN Field Validation")
@pytest.mark.parametrize("firstname",["Kanish"])
def test_gstin_fifteen_char(driver,firstname):
    # logger.info("Customer GSTIN Field Testing")
    row = 11
    customer_gstin = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Customer GSTIN Number should be 15 Characters"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.check_customer_gstin_number(customer_gstin, firstname)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To verify valid email address for the customer..")
@allure.description("To verify valid email address for the customer..")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_0010")
@allure.story("Email Field Validation.")
@pytest.mark.parametrize(
    "firstname,lastname,gstin,phoneno",
    [
        ("Manish","S","33SGETWBAH42AX","7845124578")
    ]
)
def test_customer_emailid_valid_one(driver,firstname,lastname,gstin,phoneno):
    row = 12
    email_id = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"The customer '{firstname}' is added successfully."
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.submit_form(firstname,lastname,gstin,email_id,phoneno)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"


@allure.title("To verify Invalid email address should not be allowed..")
@allure.description("To verify Invalid email address should not be allowed..")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_0011")
@allure.story("Email Field Validation.")
@pytest.mark.parametrize(
    "firstname,lastname,gstin,phoneno",
    [
        ("Manish","S","33SGETWBAH42AX","7845124578")
    ]
)
def test_customer_emailid_invalid_one(driver,firstname,lastname,gstin,phoneno):
    row = 13
    email_id = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Invalid gmail"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.email_validation(firstname,lastname,gstin,email_id,phoneno)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"

@allure.title("To verify the email address field should not be allowed for the mobile number")
@allure.description("To verify the email address field should not be allowed for the mobile number")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_0012")
@allure.story("Email Field Validation.")
@pytest.mark.parametrize(
    "firstname,lastname,gstin,phoneno",
    [
        ("Manish","S","33SGETWBAH42AX","7845124578")
    ]
)
def test_customer_emailid_invalid_two(driver,firstname,lastname,gstin,phoneno):
    row = 14
    email_id = read_data(file_path, "Cus-Data-Test-Case", row, 3)
    expected_msg = f"Invalid gmail"
    form_page = CustomerDetails(driver)
    form_page.site_url()
    response = form_page.email_validation(firstname,lastname,gstin,email_id,phoneno)
    print("response", response)
    result = "Pass" if response == expected_msg else "Fail"
    write_data(file_path,'Cus-Data-Test-Case',row,5, response,6,result)
    assert response == expected_msg, f"Expected '{expected_msg}', but got '{response}'"