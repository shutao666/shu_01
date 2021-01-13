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
    def test_01plsc(self):
        #批量生成防伪码
        try:
            self.driver.find_element(By.NAME, "Username").send_keys("admin")
            self.driver.find_element(By.NAME, "Password").send_keys("admin999")
            time.sleep(5)
            self.driver.find_element(By.XPATH, "/html/body/div/section/form/div/input[3]").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,"/html/body/section/aside/div/ul/li[2]/a/span[1]").click()
            self.driver.find_element(By.XPATH,"/html/body/section/aside/div/ul/li[2]/ul/li[1]/a").click()
            time.sleep(1)
            self.driver.find_element(By.NAME,"riqi").clear()
            self.driver.find_element(By.NAME,"riqi").send_keys("202101041032453")
            self.driver.find_element(By.NAME, "code_length").clear()
            self.driver.find_element(By.NAME,"code_length").send_keys("12")
            select1=d.driver.find_element(By.XPATH,"//*[@id='code_type']")
            Select(select1).select_by_index(2)
            time.sleep(2)
            select2=d.driver.find_element(By.XPATH,"//*[@id='txm_type']")
            Select(select2).select_by_index(1)
            time.sleep(2)
            self.driver.find_element(By.NAME,"txm_num").send_keys("8")
            self.driver.find_element(By.NAME,"code_count").send_keys("1")
            self.driver.find_element(By.CLASS_NAME,"searchable-select-caret").click()
            self.driver.find_element(By.CLASS_NAME,"searchable-select-item").click()
            self.driver.find_element(By.CSS_SELECTOR,".searchable-select-caret").click()
            self.driver.find_element(By.CLASS_NAME,"searchable-select-item").click()
            select5=d.driver.find_element(By.XPATH,"//*[@id='qiyong']")
            Select(select5).select_by_value("no")
            time.sleep(2)
            self.driver.find_element(By.ID, "tj").click()
            time.sleep(3)
            real=d.driver.find_element(By.CSS_SELECTOR,".layui-layer-content").text
            yuqi="恭喜，已成功生成1个防伪码！"
            self.assertEqual(real,yuqi,msg="失败了")
        except Exception as e:
            print("error",e)
if __name__ == '__main__':
    unittest.main()
