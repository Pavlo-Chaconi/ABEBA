from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

exec_path = "driver/chromedriver.exe"


class TestStrCalc:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)
        self.driver.get("https://testsheepnz.github.io/random-number.html")

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_dice_page(self):
        self.driver.maximize_window()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        current_scrollTop = self.driver.execute_script('return document.body.scrollTop;')
        current_clientHeight = self.driver.execute_script('return document.body.clientHeight;')
        all_scroll_height = self.driver.execute_script('return document.body.scrollHeight;')
        assert current_clientHeight + current_scrollTop == all_scroll_height

        element_of_builds = self.driver.find_element_by_id("buildNumber")
        drop_down_menu_builds = Select(element_of_builds)
        drop_down_menu_builds.select_by_visible_text("Demo")
        drop_down_menu_builds_value = self.driver.execute_script(
            "var elem = document.getElementById('buildNumber');"
            "return elem.options[elem.selectedIndex].text")
        assert drop_down_menu_builds_value == "Demo"

        self.driver.find_element_by_id("rollDiceButton").click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        current_scrollTop = self.driver.execute_script('return document.body.scrollTop;')
        current_clientHeight = self.driver.execute_script('return document.body.clientHeight;')
        all_scroll_height = self.driver.execute_script('return document.body.scrollHeight;')
        assert current_clientHeight + current_scrollTop == all_scroll_height

        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="numberGuess"]').send_keys("string")
        dice_field_value = str(self.driver.execute_script(
            f"return document.getElementById('numberGuess').value;"))
        assert dice_field_value == "string"

        self.driver.find_element_by_id("submitButton").click()

        assert self.driver.find_element_by_xpath('//*[@id="feedbackLabel"]/font/b/i').text == "string: Not a number!"


