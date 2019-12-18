def get_diver():
    from appium import webdriver
    desired_caps = dict()
    desired_caps["platformName"] = "android"
    desired_caps["platformVersion"] = "5"
    desired_caps["deviceName"] = "***"  # 安卓设备名称可以不写
    desired_caps["appPackage"] = "com.android.settings"
    desired_caps["appActivity"] = ".Settings"
    desired_caps["resetKeyboard"] = True  # 重置设备的输入键盘
    desired_caps["unicodeKeyboard"] = True  # 采用unicode码输入
    # desired_caps["noReset"] = True #重置app
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver
