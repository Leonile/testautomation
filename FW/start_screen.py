import time

from FW.fw_mobile_base import FwMobileBase

class Locator:
    button_skip = '//android.widget.Button[@content-desc="Пропустить"]'
    skip_tutorial = '//android.widget.EditText'


class StartScreen(FwMobileBase):

    def click_button_skip(self):
        self.click_by_xpath(Locator.button_skip)
        return self.manager.schedule_screen

