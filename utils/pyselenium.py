from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
class Pyselenium():
    #初始化浏览器驱动
    def __init__(self,browers='Chrome'):
        if browers=='Chrome':
            driver=webdriver.Chrome(r"C:/Users/eagle/Desktop/practise/practice0622/drivers/chromedriver.exe")
        elif browers=='edge':
            driver=webdriver.Edge()
        else:
            print('浏览器错误，请确认')
        self.driver=driver
    #返回driver
    def getDriver(self):
        return self.driver
    #打开URL
    def openUrl(self,url):
        self.driver.get(url)

    #最大化浏览器窗口
    def maxWindows(self):
        self.driver.maximize_window()

    #通过不同的方式查找界面元素
    def findElement(self,by,value):
        if by == 'id':
            locator= (by,value)
            element =WebDriverWait(self.getDriver(),19).until(lambda s: s.find_element(*locator))
            return element
        elif by == 'name':
            locator= (by,value)
            element =WebDriverWait(self.getDriver(),19).until(lambda s: s.find_element(*locator))
            return element
        elif by == 'xpath':
            element =self.driver.find_element_by_xpath(value)
            return element
        elif by == 'css':
            element =self.driver.find_element_by_css_selector(value)
            return element
        elif by == 'classname':
            element =self.driver.find_element_by_class_name(value)
            return element
        elif by == 'link_test':
            element =self.driver.find_element_by_link_text(value)
            return element
        elif by == 'partial_link_text':
            element =self.driver.find_element_by_partial_link_text(value)
            return element
        elif by == 'tag_name':
            element =self.driver.find_element_by_tag_name(value)
            return element
        else:
            print('无对应方法，请检查')
            return None

    #给指定元素发送值
    def sendkeys(self,by,value,keys_values):
        self.findElement(by,value).send_keys(keys_values)

    #点击页面元素
    def clickElement(self,by,value):
        self.findElement(by,value).click()

    #鼠标悬停
    def hover(self,by,value):
        element=self.findElement(by,value)
        ActionChains(self.driver).move_to_element(element).perform()

    #获取标题
    def getTitle(self):
        return self.driver.title


    #退出浏览器
    def quit(self):
        self.driver.quit()


