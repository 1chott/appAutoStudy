from appium import webdriver

# 设备连接前置配置
descried_cap = dict()

descried_cap["platformName"] = "android"
descried_cap["platformVersion"] = "5.1.1"
descried_cap["deviceName"] = "emulator-5554"
descried_cap["appPackage"] = "com.ss.android.ugc.aweme"
descried_cap["appActivity"] = ".main.MainActivity"

# 实例化driver驱动对象 # 注意url不要写错
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', descried_cap)

# 查询启动名 包名
print(driver.current_activity)  # 获取当前启动名
print(driver.current_package)   # 获取当前包名
print(driver.current_context)   # 查询手机上下文之间环境 native_app 原生app

