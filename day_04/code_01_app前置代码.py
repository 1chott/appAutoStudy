# 导入python需要的webdriver库
from appium import webdriver

# 定义一个空字典存放具体的配置参数
desired_caps = dict()

# 书写具体的参数
desired_caps["platformName"] = "android"    # 当前的系统平台名称
desired_caps["platformVersion"] = "5.1.1"   # 当前连接设备的 android 版本
desired_caps["deviceName"] = "****"   # 当前已连接设备的名称 安卓设备名称可以不写 通过adb devices 查看 emulator-5554
desired_caps["appPackage"] = "com.android.settings"     # 被测试App包名
desired_caps["appActivity"] = ".Settings"    # 被测试App的启动名

# 获取对应连接对象  (Appium-server url 默认端口号4723)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
