import time

from Test.mobile_base import MobileBase


class TestMobile(MobileBase):

    def test_run(self):
        surname = 'Мещеряков'
        # Пропускаем стартовый экран
        schedule_screen = self.APP.start_screen.click_button_skip()
        # Нажимаем на поле ввода
        schedule_screen.click_input_search()
        # Вводим значение
        schedule_screen.send_keys_in_search(surname)
        assert surname in schedule_screen.get_text_from_search_placeholder()