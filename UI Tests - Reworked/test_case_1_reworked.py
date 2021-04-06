from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

exec_path = "driver/chromedriver.exe"


class TestNumCalc:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)
        self.driver.get("https://testsheepnz.github.io/BasicCalculator.html")

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_calc(self):
        self.driver.maximize_window()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        current_scrollTop = self.driver.execute_script('return document.body.scrollTop;')
        current_clientHeight = self.driver.execute_script('return document.body.clientHeight;')
        all_scroll_height = self.driver.execute_script('return document.body.scrollHeight;')
        assert current_clientHeight + current_scrollTop == all_scroll_height

        element_of_drop_down_menu = self.driver.find_element_by_id("selectBuild")
        drop_down_menu_builds = Select(element_of_drop_down_menu)
        drop_down_menu_builds.select_by_visible_text("Prototype")
        drop_down_menu_builds_value = self.driver.execute_script(
            "var elem = document.getElementById('selectBuild');"
            "return elem.options[elem.selectedIndex].text")
        assert drop_down_menu_builds_value == 'Prototype'

        self.driver.find_element_by_id("number1Field").send_keys(2)
        first_num_value = int(self.driver.execute_script(
            f"return document.getElementById('number1Field').value;"))
        assert first_num_value == 2

        self.driver.find_element_by_id("number2Field").send_keys(3)
        second_num_value = int(self.driver.execute_script(
            f"return document.getElementById('number2Field').value;"))
        assert second_num_value == 3

        element_of_operation_menu = self.driver.find_element_by_id("selectOperationDropdown")
        drop_down_menu_operations = Select(element_of_operation_menu)
        drop_down_menu_operations.select_by_visible_text("Subtract")
        drop_down_menu_value = self.driver.execute_script(
            "var elem = document.getElementById('selectOperationDropdown');"
            "return elem.options[elem.selectedIndex].text")
        assert drop_down_menu_value == 'Subtract'

        self.driver.find_element_by_id("calculateButton").click()

        answer_value = int(self.driver.execute_script(
            f"return document.getElementById('numberAnswerField').value;"))
        assert answer_value == -1
