from appium import webdriver

import time
# 设置配置文件
descried_caps = dict()

descried_caps["platformName"] = "android"
descried_caps["platformVersion"] = "5.1.1"
descried_caps["deviceName"] = "emulator-5554"
descried_caps["appPackage"] = "com.bjcsxq.chat.carfriend"
descried_caps["appActivity"] = ".MainActivity"

# 实例化连接驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", descried_caps)

# 将app退到后台x秒后再打开
# driver.background_app(3)

# 获取分辨率 ， 返回一个字典 {'width': 720, 'height': 1280}
resolution = driver.get_window_size()
print("分辨率为： ", resolution)

# 模拟键盘操作 通过keyevent值操作 3home键 4返回键  66回车
driver.keyevent(3)
# 截图
driver.get_screenshot_as_file("./2.png")

time.sleep(3)
# 截图.png格式 有界面切换的时候加一个强制等待，否则执行太快还没切换的时候就截图了
driver.get_screenshot_as_file("./1.png")

# 关闭资源
driver.quit()
