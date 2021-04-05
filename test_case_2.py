from selenium import webdriver
from selenium.webdriver.support.ui import Select

def main():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://testsheepnz.github.io/BasicCalculator.html")

    element_of_builds = driver.find_element_by_id("selectBuild")
    drop_down_menu_builds = Select(element_of_builds)
    drop_down_menu_builds.select_by_visible_text("Prototype")

    first_str_field_elem = driver.find_element_by_id("strber1Field")
    first_str_field_elem.send_keys("gs")

    second_str_field_elem = driver.find_element_by_id("strber2Field")
    second_str_field_elem.send_keys("bu")

    element_of_operation_menu = driver.find_element_by_id("selectOperationDropdown")
    drop_down_menu_operations = Select(element_of_operation_menu)
    drop_down_menu_operations.select_by_visible_text("Concatenate")

    button = driver.find_element_by_id("calculateButton")
    button.click()

    third_str_field_elem = driver.find_element_by_id("numberAnswerField")
    if third_str_field_elem.get_property("value") == "gsbu":
        print("Тест пройден!")

    else:
        print("Тест не пройден!")

if __name__ == "__main__":
    main()