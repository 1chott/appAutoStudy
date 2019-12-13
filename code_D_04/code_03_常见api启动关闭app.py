import time

from appium import webdriver

# 设备连接前置配置
descried_caps = dict()

descried_caps["platformName"] = "android"
descried_caps["platformVersion"] = "5.1.1"
descried_caps["deviceName"] = "emulator-5554"
descried_caps["appPackage"] = "com.bjcsxq.chat.carfriend"
descried_caps["appActivity"] = ".MainActivity"

# 实例化driver驱动对象 # 注意url不要写错
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', descried_caps)

time.sleep(3)
# 将app退到后台
driver.close_app()

time.sleep(3)
# 启动app （包名， 启动名）
driver.start_activity("com.ss.android.ugc.aweme", ".main.MainActivity")
print(driver.current_package)

time.sleep(3)

# 关闭driver对象（关闭了连接对象）
driver.quit()

