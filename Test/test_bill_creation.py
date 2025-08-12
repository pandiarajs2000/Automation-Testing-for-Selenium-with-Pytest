import time
import pytest
import allure
from utils.log_utils import logger
from utils.utils import read_data, write_data, row_count, read_all_data
from Pages.bill_creation_page import BillCreation

@allure.title("Verify the add row button")
@allure.description("Verify the add row button")
@allure.severity(allure.severity_level.MINOR)
@allure.testcase("TC_001")
@allure.story("Test Add Row Button")
def test_add_row_btn(driver):
    print("Add row button click..")
    form_page = BillCreation(driver)
    form_page.page_url()
    res = form_page.click_add_row_btn()
    print(res)

@allure.title("To verify the add row and added the data")
@allure.description("To verify the add row and added the data")
@allure.severity(allure.severity_level.MINOR)
@allure.testcase("TC_002")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty,rate", [("PRO-008-Orange","3","240")])
def test_add_row_btn_select_data(driver, product_id, qty, rate):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.add_line_item(product_id, qty, rate)
    time.sleep(10)

@allure.title("To verify the new product should not be allowed in the select field")
@allure.description("To verify the new product should not be allowed in the select field")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_003")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty,rate", [("PRO-009-Curd","3","20")])
def test_select_field(driver, product_id, qty, rate):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.add_line_item(product_id, qty, rate)
    time.sleep(10)

@allure.title("To verify the Product Name field should not be edited")
@allure.description("To verify the Product Name field should not be edited")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_004")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,product_name,qty,rate", [("OILL","OILL","3","20")])
def test_product_name_field(driver, product_id,product_name, qty, rate):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.add_line_item(product_id,product_name, qty, rate)
    time.sleep(10)

@allure.title("To verify the qty field key up")
@allure.description("To verify the qty field key up")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_005")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty,rate", [("OILLL","3","20")])
def test_qty_field_validation(driver, product_id, qty, rate):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.qty_field_validate(product_id, qty, rate)
    time.sleep(10)

@allure.title("To verify the qty for decimal point")
@allure.description("To verify the qty for decimal point")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_006")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty,rate", [("OILLL","3.555000","20")])
def test_qty_field_validate_decimal(driver, product_id, qty, rate):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.qty_field_validate(product_id, qty, rate)
    time.sleep(10)

@allure.title("To verify the qty field should not be allow not string value")
@allure.description("To verify the qty field should not be allow not string value")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_007")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty,rate", [("OILLL","RRR","20")])
def test_qty_field_validate_string(driver, product_id, qty, rate):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.qty_field_validate(product_id, qty, rate)
    time.sleep(10)

@allure.title("To verify the category field should not be edited")
@allure.description("To verify category qty field should not be allow not string value")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_008")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty,rate,category", [("OILLL","3","20","OILLL")])
def test_category_field_validation(driver, product_id, qty, rate,category):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.category_field_validate(product_id, qty, rate,category)
    time.sleep(10)

@allure.title("To verify the total field should not be edited")
@allure.description("To verify total qty field should not be allow not string value")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_009")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty", [("OILLL","3")])
def test_total_field_validation(driver, product_id, qty):
    print("Add row button click..")
    logger.info("Test Working")
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    response = form_page.total_field_validate(product_id, qty)
    print("Response", response)
    time.sleep(10)
    assert response != "NaN", f"Total field displayed as NaN for product {product_id}"

@allure.title("To verify the muliple rows added and capture the screenshot")
@allure.description("To verify the muliple rows added and capture the screenshot")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_0010")
# @pytest.mark.parametrize("product_id,qty,rate", [("PRO-008-Orange","3","240"),("PRO-006-Dates","3","240")])

@pytest.mark.parametrize(
    "items",
    [
        [
            ("PRO-008-Orange","3","240"),
            ("PRO-006-Dates","3","240")
        ]
    ]
)
def test_multiple_row_added(driver, items):
    form_page = BillCreation(driver)
    form_page.page_url()
    for product_id, qty, rate in items:
        form_page.click_add_row_btn()
        form_page.add_line_item(product_id, qty, rate)
    time.sleep(20)

@allure.title("To verify the delete the single row")
@allure.description("To verify the delete the single row")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("TC_009")
@allure.story("Test Add Row Button")
@pytest.mark.parametrize("product_id,qty,rate", [("OILLL","3","123")])
def test_delete_field_validation(driver, product_id, qty, rate):
    form_page = BillCreation(driver)
    form_page.page_url()
    form_page.click_add_row_btn()
    form_page.add_line_item(product_id, qty, rate)
    delete_row = driver.get_screenshot_as_png()
    allure.attach(delete_row,name="Delete Row", attachment_type=allure.attachment_type.PNG)
    form_page.delete_the_row()
    time.sleep(20)