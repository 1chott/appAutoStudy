from appium import webdriver

# 设备连接前置配置
descried_cap = dict()

descried_cap["platformName"] = "android"
descried_cap["platformVersion"] = "5.1.1"
descried_cap["deviceName"] = "emulator-5554"
descried_cap["appPackage"] = "com.bjcsxq.chat.carfriend"
descried_cap["appActivity"] = ".MainActivity"

# 实例化driver驱动对象 # 注意url不要写错
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', descried_cap)

# 判断app是否已经被安装 传入的是 包名 返回布尔值
print(driver.is_app_installed("com.bjcsxq.chat.carfriend"))
