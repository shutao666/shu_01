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
    def test_03cpxz(self):
        # 产品条码有重复！
        try:
            self.driver.find_element(By.NAME, "Username").send_keys("admin")
            self.driver.find_element(By.NAME, "Password").send_keys("admin999")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "/html/body/div/section/form/div/input[3]").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.driver.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/ul/li[1]/a").click()
            time.sleep(2)
            self.driver.find_element(By.NAME, "pro_name").send_keys("武大郎烧饼")
            self.driver.find_element(By.NAME, "cpbh").send_keys("355278525")
            self.driver.find_element(By.NAME, "cptxm").send_keys("1329569")
            self.driver.find_element(By.CSS_SELECTOR, ".ke-edit-iframe").send_keys("真的太好吃了")
            time.sleep(2)
            self.driver.find_element(By.XPATH,"/html/body/section/section/section/div/div/section/div/form/div[9]/div/button").click()
            real = d.driver.find_element(By.XPATH, "/html/body/div[3]/div").text
            yuqi = "产品条码有重复!"
            self.assertEqual(real, yuqi, msg="断言失败")
        except Exception as e:
            print("error", e)
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()