import unittest
from selenium import webdriver
import time
class qqemil(unittest.TestCase):
    def setUp(self):
        self.login=webdriver.Firefox()
        self.login.get("https://mail.qq.com/")
        time.sleep(3)
    def tearDown(self):
        self.login.close()
        self.login.quit()
    def test_qq(self):
        self.login.switch_to.frame("login_frame")
        # self.login.find_element_by_id("switcher_plogin").click()
        self.login.find_element_by_name("u").send_keys("1308391552")
        time.sleep(1)
        self.login.find_element_by_name("p").send_keys("st1308391552")
        self.login.find_element_by_id("login_button").click()
        self.login.switch_to.default_content()
        time.sleep(3)
        self.login.find_element_by_partial_link_text("写信").click()
        time.sleep(2)
        self.login.find_element_by_xpath("/html/body").send_keys("今天你学习了吗")
        time.sleep(2)
        self.login.switch_to.frame("mainFrame")
        self.login.find_element_by_xpath("/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input").send_keys("417725811@qq.com")
        self.login.find_element_by_xpath("//*[@id='subject']").send_keys("笔记本")
        self.login.find_element_by_xpath("/html/body/form[2]/div[3]/div/a[1]").click()
        self.login.switch_to.default_content()
        time.sleep(2)



if __name__ == '__main__':
    unittest.main()