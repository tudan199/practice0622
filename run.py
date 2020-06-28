from utils.HTMLTestRunner import HTMLTestRunner
import unittest
import time
filename=time.strftime('%Y-%m-%d-%H-%M-%S')

filepath=r"C:/Users/eagle/Desktop/practise/practice0622/report/"+ filename +'.html'
print(filepath)
testcases = unittest.defaultTestLoader.discover(r'C:\Users\eagle\Desktop\practise\practice0622\testcases','test*.py')
testsuite= unittest.TestSuite()
testsuite.addTests(testcases)
with open(filepath,'wb') as f:
    runner = HTMLTestRunner(stream=f,verbosity=2,title='报告名称',description='报告描述')
    runner.run(testsuite)