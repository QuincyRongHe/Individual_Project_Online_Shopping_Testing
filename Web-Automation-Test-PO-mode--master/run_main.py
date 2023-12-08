
import unittest
import time
from tool.HTMLTestRunner import HTMLTestRunner


suite = unittest.defaultTestLoader.discover("./scripts")
# report directory
dir_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# run report
with open(dir_path, "wb") as f:
    HTMLTestRunner(stream=f, title="Trading System Automated Test Report").run(suite)