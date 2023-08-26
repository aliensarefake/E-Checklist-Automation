from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

def automate(link):
    driver = webdriver.Chrome()
    driver.get(link)

    #find all the checkboxes
    checkboxes = driver.find_elements(By.CLASS_NAME, 'chakra-checkbox') # Using new syntax with By
    for checkbox in checkboxes:
        checkbox.click()

    #find all input field elements
    elements = driver.find_elements(By.CSS_SELECTOR, ".chakra-form-control")
    for element in elements:
        try:
            inner_div = element.find_element(By.CSS_SELECTOR, "div.css-1l6dwoh")
            label_element = inner_div.find_element(By.CSS_SELECTOR, "label")        
            p_element = label_element.find_element(By.CSS_SELECTOR, "p.chakra-text")
            p_text = p_element.text
            match = re.search(r'(Phy Qty|Phy Quantity|Quantity) = (\d+)', p_text)
            if match:
                qty = match.group(2)  
                input_div = element.find_element(By.CSS_SELECTOR, "div.css-hd3jvf")
                input_field = input_div.find_element(By.TAG_NAME, "input")    
                input_field.clear()
                input_field.send_keys(qty)

        except:
            print('not present')   


    driver.execute_script("window.scrollTo(0, 0);") #scroll back up (manually key in the remaining details)
    time.sleep(10000000) #prevent chromedriver from closing