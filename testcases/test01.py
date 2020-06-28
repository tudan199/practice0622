import sys
sys.path.append('c:\\Users\\eagle\\Desktop\\practise\\practice0622')
from utils.pyselenium import Pyselenium
from utils.readExcel import readExcel
from utils.HTMLTestRunner import HTMLTestRunner
import utils.webConfig
import unittest,time
from selenium.webdriver.common.keys import Keys

class BaiduTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.py=Pyselenium('Chrome')

    @classmethod
    def tearDownClass(cls):
        cls.py.quit()

    def testbaidu(self):
        self.py.openUrl('http://www.baidu.com')
        testfilepath='C:/Users/eagle/Desktop/practise/practice0622/data/test.xls'
        self.keys=readExcel(testfilepath,0,0)
        
        self.py.sendkeys('id','kw',str(self.keys))
        self.py.maxWindows()
        self.py.clickElement('id','su')
        #百度登录，并判断是否正常登录
        # self.py.clickElement('name','tj_login')
        # self.py.clickElement('id','TANGRAM__PSP_11__footerULoginBtn')
        # print('用户名为%s,密码为%s'%(readExcel(testfilepath,1,0),readExcel(testfilepath,1,1)))
        # self.py.sendkeys('name','userName',readExcel(testfilepath,1,0))
        # self.py.sendkeys('name','password',readExcel(testfilepath,1,1))
        
        # self.py.clickElement('id','TANGRAM__PSP_11__submit')
        # # assert self.py.findElement('link_text','末了199')
        # self.py.hover('id','user')
        
        # ele1=self.py.findElement('xpath','//*[@id="s_user_name_menu"]/div/a[4]')
        # if ele1 != None:
        #     assert 1==1
        # else:
        #     assert 1==0
        time.sleep(6)
if __name__=='__main__':
    unittest.main()