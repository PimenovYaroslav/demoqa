from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage


class SliderPage(BasePage):
    """
    Page Object for the Slider page (DemoQA).
    Provides methods to interact with the slider.
    """

    SLIDER_INPUT = (By.CSS_SELECTOR, "input[type='range']")
    SLIDER_VALUE = (By.ID, "sliderValue")

    def __init__(self, driver):
        super().__init__(driver)

    def get_slider_value(self) -> int:
        """
        Returns the current value of the slider.
        """
        value = self.get_element_value(self.SLIDER_VALUE)
        return int(value)

    def move_slider_with_keys(self, target_value: int):
        """
        Moves the slider to the target value using keyboard arrows
        and waits for the value to be updated.
        """
        slider = self.find_element(self.SLIDER_INPUT)

        current_value = int(slider.get_attribute("value"))
        value_offset = target_value - current_value

        if value_offset > 0:
            for _ in range(value_offset):
                slider.send_keys(Keys.ARROW_RIGHT)
        else:
            for _ in range(abs(value_offset)):
                slider.send_keys(Keys.ARROW_LEFT)

        self.wait_for_element_value_to_be_updated(self.SLIDER_VALUE, str(target_value))
