import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, feature):
        # 如果元素找不到 使用显示等待 尝试查找
        # 最终元素不存在 使用捕获错误 返回None   如果元素存在就返回元素对象
        try:
            wait = WebDriverWait(self.driver, 5, 1)
            obj = wait.until(lambda x: x.find_element(*feature))
        except:
            return None
        else:
            return obj

    # 封装一个先找大盒子的对象 在找小盒子元素对象
    def get_ele_ancestry(self, ancestry, sub):
        # 先找大盒子的对象  找到就返回对象 如果找不到就返回None
        # 在判断找小盒子元素  传递一个元素信息  从大盒子对象开始查找 如果找到就返回对象
        # 如果找不到就尝试显示等待 最终没有找到就返回None
        ancestry_obj = self.get_element(ancestry)
        try:
            wait = WebDriverWait(ancestry_obj, 5, 1)
            obj = wait.until(lambda x: x.find_element(*sub))
        except:
            return None
        else:
            return obj

    def execute_tap(self, feature):
        # 既可以接受对象直接进行点击操作
        # 也可以接受元组特征 (元组 ), 先通过特征找到对象 再执行操作
        # 因为我们移动端推荐使用 touchaction 类里面轻敲事件
        action = TouchAction(self.driver)
        if isinstance(feature, tuple):
            feature = self.get_element(feature)
        # feature.click()
        action.tap(feature).perform()

    def execute_input(self, feature, val):
        # 既可以接受对象直接进行输入操作
        # 也可以接受元组特征 (元组 ), 先通过特征找到对象 再执行输入操作
        if isinstance(feature, tuple):
            feature = self.get_element(feature)
        feature.send_keys(val)

    def get_size(self, ):
        obj = self.driver.get_window_size()
        return obj["width"], obj["height"]

    def swipe_left(self, count):
        # 封装一个滑屏动作 需要传递滑动次数
        w, h = self.get_size()
        for i in range(count):
            self.driver.swipe(w * 0.9, h * 0.5, w * 0.1, h * 0.5)
            time.sleep(1)

    def swipe_top(self, count, ms):
        # 封装一个滑屏动作 需要传递滑动次数
        w, h = self.get_size()
        for i in range(count):
            self.driver.swipe(w * 0.5, h * 0.9, w * 0.5, h * 0.1, ms)
            time.sleep(1)

    def find_ele_recursion(self, feature):
        # 因为我们在查找元素的时候 经常遇到一屏展示不到元素
        # 需要滑屏查找是否存在元素 如果滑屏一次能找到就返回obj
        # 如果滑屏一次找不到就在滑屏一次
        obj = self.get_element(feature)
        if obj:
            return obj
        else:
            self.swipe_top(1, 4000)
            time.sleep(1)
            return self.find_ele_recursion(feature)
