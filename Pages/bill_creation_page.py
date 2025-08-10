from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class BillCreation:
    def __init__(self, driver):
        self.driver = driver
        self.add_row_btn = (By.XPATH, "//button[@class='btn btn-success w-100']")
        self.delete_btn = (By.XPATH, "//button[@class='btn btn-danger w-100']")
        self.save_btn = (By.XPATH, "//button[@class='btn btn-primary w-100']")
        self.title = (By.XPATH, "//form/preceding-sibling::h4")
        self.table_xpth = (By.XPATH, "//form/descendant::table[@id='productTable']")
        self.table_row_xpath = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr")
        self.table_row_data_xpath = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td")
        self.td_select_option = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::select[@class='form-select product-id']")
        self.td_first_index = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::input[@type='checkbox']")
        self.td_select_prod = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::select")
        self.td_product_name = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::input[@type='text' and @class='form-control product-name']")
        self.td_qty = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::input[@type='number' and @class='form-control qty']")
        self.td_rate = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::input[@type='number' and @class='form-control rate']")
        self.td_category = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::input[@type='text' and @class='form-control category']")
        self.td_total = (By.XPATH, "//form/descendant::table[@id='productTable']/descendant::tbody/descendant::tr//td/descendant::input[@type='text' and @class='form-control total']")
        self.product_name_xpath = (By.XPATH, "//form/descendant::tbody//tr//td//input[@type='number' and contains(@class, 'form-control qty')]")
        self.category_xpath = (By.XPATH, "//form/descendant::tbody//tr//td//input[@type='text' and contains(@class, 'form-control category')]")
        self.total_xpath = (By.XPATH, "//form/descendant::tbody//tr//td//input[@type='text' and contains(@class, 'form-control total')]")
        self.check_box_xpath = (By.XPATH, "//form/descendant::tbody//tr//td//input[@type='checkbox']")

    
    def page_url(self):
        url = self.driver.get('http://127.0.0.1:5000/bill_creation')
        time.sleep(5)
        return url
    
    def click_add_row_btn(self):
        self.driver.implicitly_wait(10)
        title = self.driver.find_element(*self.title).text
        self.driver.find_element(*self.add_row_btn).click()
        time.sleep(3)
        return title
    
    def add_line_item(self, product_id, qty, rate):
        self.driver.implicitly_wait(10)

        # rows=self.driver.find_elements(*self.table_row_xpath)
        rows = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.table_row_xpath))
        last_rows = rows[-1]

        tds = last_rows.find_elements(*self.table_row_data_xpath)
        
        # fill the select product
        select_element = Select(tds[1].find_element(*self.td_select_option))
        select_element.select_by_visible_text(product_id)

        # set qty
        self.driver.find_element(*self.td_qty).clear()
        self.driver.find_element(*self.td_qty).send_keys(qty)

        # set rate
        self.driver.find_element(*self.td_rate).clear()
        self.driver.find_element(*self.td_rate).send_keys(rate)

        time.sleep(20)

    def qty_field_validate(self, product_id, qty=None, rate=None):
        self.driver.implicitly_wait(10)
        self.driver.last_row = [-1]
        rows=self.driver.find_elements(*self.table_row_xpath)
        tds = self.driver.find_elements(*self.table_row_data_xpath)

        # fill the select product
        select_element = Select(tds[1].find_element(*self.td_select_option))
        select_element.select_by_visible_text(product_id)

        # set qty
        self.driver.find_element(*self.td_qty).clear()
        self.driver.find_element(*self.td_qty).send_keys(qty)

        # set rate
        self.driver.find_element(*self.td_rate).clear()
        self.driver.find_element(*self.td_rate).send_keys(rate)

        time.sleep(10)

    def rate_field_validate(self, product_id, qty=None, rate=None):
        self.driver.implicitly_wait(10)
        self.driver.last_row = [-1]
        rows=self.driver.find_elements(*self.table_row_xpath)
        tds = self.driver.find_elements(*self.table_row_data_xpath)

        # fill the select product
        select_element = Select(tds[1].find_element(*self.td_select_option))
        select_element.select_by_visible_text(product_id)

        # set qty
        self.driver.find_element(*self.td_qty).clear()
        self.driver.find_element(*self.td_qty).send_keys(qty)

        # set rate
        self.driver.find_element(*self.td_rate).clear()
        self.driver.find_element(*self.td_rate).send_keys(rate)

        time.sleep(10)

    # category field validation
    def category_field_validate(self, product_id, product_name=None, qty=None, rate=None, category=None):
        self.driver.implicitly_wait(10)
        self.driver.last_row = [-1]
        rows=self.driver.find_elements(*self.table_row_xpath)
        tds = self.driver.find_elements(*self.table_row_data_xpath)

        # fill the select product
        select_element = Select(tds[1].find_element(*self.td_select_option))
        select_element.select_by_visible_text(product_id)

        # set qty
        self.driver.find_element(*self.td_qty).clear()
        self.driver.find_element(*self.td_qty).send_keys(qty)

        # set rate
        self.driver.find_element(*self.td_rate).clear()
        self.driver.find_element(*self.td_rate).send_keys(rate)

        # set category
        self.driver.find_element(*self.category_xpath).clear()
        self.driver.find_element(*self.category_xpath).send_keys(category)


        total_value = self.driver.find_element(*self.total_xpath).get_attribute('value').strip()
        if total_value == "NaN":
            print("total value", total_value)
            time.sleep(5)
            self.driver.get_screenshot_as_file("E:\\Frappe Model Project\\Screen Shots\\NaN_Type.png")
        time.sleep(10)
        return total_value
    
    def total_field_validate(self, product_id, qty):
        self.driver.implicitly_wait(10)
        self.driver.last_row = [-1]
        rows=self.driver.find_elements(*self.table_row_xpath)
        tds = self.driver.find_elements(*self.table_row_data_xpath)

        # fill the select product
        select_element = Select(tds[1].find_element(*self.td_select_option))
        select_element.select_by_visible_text(product_id)

        # set qty
        self.driver.find_element(*self.td_qty).clear()
        self.driver.find_element(*self.td_qty).send_keys(qty)

        total_value = self.driver.find_element(*self.total_xpath).get_attribute('value').strip()
        if total_value == "NaN":
            print("total value", total_value)
            time.sleep(5)
            self.driver.get_screenshot_as_file("E:\\Frappe Model Project\\Screen Shots\\NaN_Type.png")
        time.sleep(10)
        return total_value
    
    def delete_the_row(self):
        self.driver.find_element(*self.check_box_xpath).click()
        self.driver.get_screenshot_as_file("E:\\Frappe Model Project\\Screen Shots\\before_delete_row.png")
        self.driver.find_element(*self.delete_btn).click()
        self.driver.get_screenshot_as_file("E:\\Frappe Model Project\\Screen Shots\\after_delete_row.png")
        time.sleep(5)