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
    def test_06sahnchu(self):
        #删除单一
        try:
            self.driver.find_element(By.NAME, "Username").send_keys("admin")
            self.driver.find_element(By.NAME, "Password").send_keys("admin999")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "/html/body/div/section/form/div/input[3]").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.driver.find_element(By.XPATH, "/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH,"/html/body/section/section/section/form/div/div/section/table/tbody/tr[5]/td[8]/span").click()
            self.driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/a[1]").click()
            time.sleep(3)
            real=d.driver.find_element(By.XPATH,"/html/body/div[3]/div").text
            yuqi="产品删除成功！"
            self.assertEqual(yuqi,real,msg="失败了啊")
        except Exception as e:
            print(e)
if __name__== '__main__':
    unittest.main()