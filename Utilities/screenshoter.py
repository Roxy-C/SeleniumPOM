import os
from datetime import datetime


class Screenshoter():

    def __init__(self, driver, screenshots_path):
        self.driver = driver
        self.dir_path = screenshots_path

    def take_screenshot(self, test_name):
        folder_prefix = datetime.now().strftime("%Y-%m-%d %H-%M")
        screenshot_suffix = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        
        try:
            if not os.path.isdir(f'{self.dir_path}\\{folder_prefix}'):
                os.mkdir(f'{self.dir_path}\\{folder_prefix}')
                self.driver.save_screenshot(f'{self.dir_path}\\{folder_prefix}\\{test_name} {screenshot_suffix}.png')
            else:
                self.driver.save_screenshot(f'{self.dir_path}\\{folder_prefix}\\{test_name} {screenshot_suffix}.png')
        except Exception:
            print('Screenshoter Error')