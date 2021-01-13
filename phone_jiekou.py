import unittest
import requests
# url="https://api.yonyoucloud.com/apis/dst/checkPhoneIfNullByMobiles/getPhoneIfNullByMobiles"
# header={
#     "apicode":"5ed099d42cb548beb6648e009fbac14a",
#     "Content-Type":"application/json"
# }
# body={"Content-Type":"application/json","mobiles":"fgfhgfhfhfgf"}
# result=requests.post(url=url,headers=header,json=body)
# print(result.text)
class Port_test(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_phone(self):
        self.url="https://api.yonyoucloud.com/apis/dst/checkPhoneIfNullByMobiles/getPhoneIfNullByMobiles"
        self.header={
            "apicode": "5ed099d42cb548beb6648e009fbac14a",
            "Content-Type": "application/json"
        }
        self.body={"Content-Type":"application/json","mobiles":"fgfhgfhfhfgf"}
        re=requests.post(url=self.url,headers=self.header,json=self.body)
        # print(re.text)
        yuqi="300004"
        self.assertIn(yuqi,re.text,msg="不存在")
if __name__ == '__main__':
    unittest.main()