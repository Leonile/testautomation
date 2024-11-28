from appium.webdriver.common.appiumby import AppiumBy

from FW.fw_mobile_base import FwMobileBase

class Locator:
    input_search = '//android.widget.EditText'


class ScheduleScreen(FwMobileBase):

    def click_input_search(self):
        self.click_by_xpath(Locator.input_search)
        return self

    def send_keys_in_search(self, text):
        self.send_keys_by_xpath(Locator.input_search, text)
        self.click_keyboard_enter()
        return self

    def get_text_from_search_placeholder(self):
        return self.get_tag_attribute(Locator.input_search, 'hint', by=AppiumBy.XPATH)
