import unittest

from selenium import webdriver

from basepage import BasePage
from Locators.nextpage_locators import NextpageLocators as NPL
from Utilities.logger import Logger
from Utilities.screenshoter import Screenshoter


class TestNextpage(unittest.TestCase, BasePage):

    @classmethod
    def setUpClass(cls):
        # Init driver and utilities
        cls.driver = webdriver.Chrome()
        cls.logger = Logger(
            'Test-NextPage', 'C:\Repos\Projects\SeleniumPOM\Tests\Logs\\')
        cls.screenshoter = Screenshoter(
            cls.driver, 'C:\Repos\Projects\SeleniumPOM\Tests\Screenshots\\')

    def setUp(self):
        # Setup driver
        self.driver.get(
            'C:\Repos\Projects\SeleniumPOM\Pages\\Nextpage.html')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_change_title(self):
        try:
            title_changer = self.driver.find_element(*NPL.btn_locator)

            self.assertEqual(self.driver.title, 'Next Page')
            title_changer.click()
            self.driver.implicitly_wait(3)
            self.assertEqual(self.driver.title, 'Finish')
            self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_first_name_input')
            self.fail()