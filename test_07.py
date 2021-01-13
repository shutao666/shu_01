from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import unittest
class mouns(unittest.TestCase):
    def setUp(self) -> None:
        self.a=webdriver.Firefox()
        self.a.get("https://www.baidu.com/index.php?tn=monline_3_dg")
    def tearDown(self) -> None:
        self.a.close()
        self.a.quit()
    def test_xuanting(self):
        self.a.maximize_window()
        ActionChains(self.a).move_to_element(self.a.find_element_by_css_selector("#s-usersetting-top")).perform()
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()
