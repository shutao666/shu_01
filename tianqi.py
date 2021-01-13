import unittest
import requests
class JiekouTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_tianqi(self):
        self.url="https://v0.yiketianqi.com/api"
        self.parms={
            "appid": "55121823",
            "appsecret": "f4XoduzQ",
            "version": "v61"
        }
        re=requests.get(url=self.url,params=self.parms)
        yuqi="咸阳"
        chengshi=re.json()["city"]
        self.assertEqual(chengshi,yuqi,msg="没找到城市")

    # @unittest.skip("")
    def test_tianqi2(self):
        self.url="https://v0.yiketianqi.com/api"
        self.parms={
            "appsecret": "f4XoduzQ",
            "version": "v61"
        }
        re=requests.get(url=self.url,params=self.parms)
        a=re.json()["errcode"]
        b=100
        self.assertEqual(a,b,msg="测试未通过")
        # print(re.json())
if __name__ == '__main__':
    unittest.main()