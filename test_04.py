import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
class Cpsy(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Firefox()
        self.driver.get("http://123.57.140.190/manage/index.php")
    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
    def test_04cpgl(self):
        #预览
        try:
            self.driver.find_element(By.NAME, "Username").send_keys("admin")
            self.driver.find_element(By.NAME, "Password").send_keys("admin999")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "/html/body/div/section/form/div/input[3]").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,"/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.driver.find_element(By.XPATH,"/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH,"/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/span").click()
            real=d.driver.find_element(By.CSS_SELECTOR,".layui-layer-title").text
            yuqi="预览"
            self.assertEqual(yuqi, real, msg="断言失败")
        except Exception as e:
            print(e)
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()