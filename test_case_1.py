from selenium import webdriver
from selenium.webdriver.support.ui import Select

def main():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://testsheepnz.github.io/BasicCalculator.html")

    element_of_builds = driver.find_element_by_id("selectBuild")
    drop_down_menu_builds = Select(element_of_builds)
    drop_down_menu_builds.select_by_visible_text("Prototype")

    first_num_field_elem = driver.find_element_by_id("number1Field")
    first_num_field_elem.send_keys(2)

    second_num_field_elem = driver.find_element_by_id("number2Field")
    second_num_field_elem.send_keys(3)

    element_of_operation_menu = driver.find_element_by_id("selectOperationDropdown")
    drop_down_menu_operations = Select(element_of_operation_menu)
    drop_down_menu_operations.select_by_visible_text("Subtract")

    button = driver.find_element_by_id("calculateButton")
    button.click()

    third_num_field_elem = driver.find_element_by_id("numberAnswerField")
    if third_num_field_elem.get_property("value") == "-1":
        print("Тест пройден!")

    else:
        print("Тест не пройден!")

if __name__ == "__main__":
    main()