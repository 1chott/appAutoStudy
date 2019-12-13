from appium import webdriver
# import os
# print(os.getcwd())

# 设备连接前置配置
descried_caps = dict()

descried_caps["platformName"] = "android"
descried_caps["platformVersion"] = "5.1.1"
descried_caps["deviceName"] = "emulator-5554"
descried_caps["appPackage"] = "com.ss.android.ugc.aweme"
descried_caps["appActivity"] = ".main.MainActivity"

# 实例化driver驱动对象 # 注意url不要写错
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', descried_caps)
driver.close_app()

# 判断app是否已经被安装 传入的是 包名 返回布尔值
if driver.is_app_installed("com.bjcsxq.chat.carfriend"):
    # 卸载app （包名）
    driver.remove_app("com.bjcsxq.chat.carfriend")
else:
    # 安装app  # 自己拉代码下来的时候记得修改路径， 翻了下源代码只能写绝对路径
    driver.install_app(r"F:\渣渣班长2\gihub代码\app\code_D_04\xuechebu_veryhuo.com.apk")

# 关闭资源
driver.quit()
