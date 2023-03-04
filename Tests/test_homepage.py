import unittest
import requests
import re
from ddt import ddt, file_data

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from basepage import BasePage
from Locators.homepage_locators import HomepageLocators as HPL
from Utilities.logger import Logger
from Utilities.screenshoter import Screenshoter


@ddt
class TestHome(unittest.TestCase, BasePage):

    @classmethod
    def setUpClass(cls):
        # Init driver and utilities
        cls.driver = webdriver.Chrome()
        cls.logger = Logger(
            'Test-Homepage', 'C:\Repos\Projects\SeleniumPOM\Tests\Logs\\')
        cls.screenshoter = Screenshoter(
            cls.driver, 'C:\Repos\Projects\SeleniumPOM\Tests\Screenshots\\')

    def setUp(self):
        # Setup driver
        self.driver.get(
            'C:\Repos\Projects\SeleniumPOM\Pages\Automation Project.html')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @file_data('C:\Repos\Projects\SeleniumPOM\Tests\Data\data.json')
    def test_first_name_input(self, first_name, **kwargs):
        """
        Test input field for first name.

        Args:
            first_name (str): The first name to be tested.

        Raises:
            AssertionError: If the field is not empty before testing, or if the input doesn't match the expected regex, or if the validity property is not raised correctly.

        """
        first_name_regex = r'^[a-zA-Z,-\.]{2,20}$'

        try:
            first_name_element = self.driver.find_element(
                *HPL.firstname_locator)

            # Check if field is empty
            self.assertEqual(
                first_name_element.get_property('value'), '', 'Field must be empty prior testing')

            # Valid input
            if (re.match(first_name_regex, first_name)):
                first_name_element.send_keys(first_name)
                # Assert field holding the value we inserted
                self.assertEqual(
                    first_name_element.get_property('value'), first_name, "Field doesn't hold the same value as sent")
                # Assert name matches regex
                self.assertTrue(re.match(first_name_regex, first_name),
                                "Input doesn't follow expected regex")
                # Assert validity property is raised per input
                self.assertTrue(
                    first_name_element.get_property("validity")["valid"], "fname field validity property raised while being correct")
                self.logger.log(self.id(), 'Passed')

            else:
                first_name_element.send_keys(first_name)
                # Assert the valid property matches the incorrect fname
                self.assertFalse(
                    first_name_element.get_property("validity")["valid"], "fname field validity property true while input incorrect")
                self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_first_name_input')
            self.fail()

    @file_data('C:\Repos\Projects\SeleniumPOM\Tests\Data\data.json')
    def test_last_name_input(self, last_name, **kwargs):
        """
        Test input field for last name.

        Args:
            last_name (str): The last name to be tested.

        Raises:
            AssertionError: If the field is not empty before testing, or if the input doesn't match the expected regex, or if the validity property is not raised correctly.

        """
        last_name_regex = r'^[a-zA-Z,-\.]{2,20}$'

        try:
            last_name_element = self.driver.find_element(*HPL.lastname_locator)

            # Check if field is empty
            self.assertEqual(
                last_name_element.get_property('value'), "")

            # Valid input
            if (re.match(last_name_regex, last_name)):
                last_name_element.send_keys(last_name)
                # Assert field holding the value we inserted
                self.assertEqual(
                    last_name_element.get_property('value'), last_name, "Field doesn't hold the same value as sent")
                # Assert name matches regex
                self.assertTrue(re.match(last_name_regex, last_name),
                                "Input doesn't follow expected regex")
                # Assert field property is valid
                self.assertTrue(
                    last_name_element.get_property("validity")["valid"], "lname field validity property raised while being correct")
                self.logger.log(self.id(), 'Passed')

            else:
                last_name_element.send_keys(last_name)
                # Assert the valid property matches the incorrect last_name
                self.assertFalse(
                    last_name_element.get_property("validity")["valid"], "lname field validity property true while input incorrect")
                self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_last_name_input')
            self.fail()

    def test_city_dropdown(self):
        """
        Test the city dropdown menu.

        Raises:
            AssertionError: If any city in the dropdown doesn't exist in the database or if the option is not selected after being clicked.

        """
        cities = ['Haifa', 'Tel Aviv', 'Jerusalem', 'Beer Sheva']
        try:
            city_dropdown = Select(self.driver.find_element(*HPL.city_locator))

            for option in city_dropdown.options:
                self.assertTrue(option.text in cities,
                                "City in dropdown doesn't exist in db")
                option.click()
                self.assertTrue(option.is_selected(),
                                "Option isn't selected after being clicked")

            self.logger.log(self.id(), 'Passed')
        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_city_dropdown')
            self.fail()

    @file_data('C:\Repos\Projects\SeleniumPOM\Tests\Data\data.json')
    def test_email_input(self, email, **kwargs):
        """
        Test input field for email.

        Args:
            email (str): The email to be tested.

        Raises:
            AssertionError: If the field is not empty before testing, or if the input doesn't match the expected regex, or if the validity property is not raised correctly.

        """
        email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{1,40}$'

        try:
            email_element = self.driver.find_element(*HPL.email_locator)

            # Check if field is empty
            self.assertEqual(
                email_element.get_property('value'), "")

            # Valid input
            if (re.match(email_regex, email)):
                email_element.send_keys(email)
                # Assert field holding the value we inserted
                self.assertEqual(email_element.get_property('value'), email)
                # Assert name matches regex
                self.assertTrue(re.match(email_regex, email))
                # Assert field property is valid
                self.assertTrue(
                    email_element.get_property("validity")["valid"])
                self.logger.log(self.id(), 'Passed')

            else:
                email_element.send_keys(email)
                # Assert the valid property matches the incorrect email
                self.assertFalse(
                    email_element.get_property("validity")["valid"])
                self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_email_input')
            self.fail()

    def test_area_dropdown(self):
        """
        Test the area dropdown functionality.

        Raises:
            AssertionError: If an exception is raised during test execution or if any of the assertions fail.
        """
        areas_prefix = ['050', '052', '053', '054']
        try:
            area_dropdown = Select(self.driver.find_element(*HPL.area_locator))

            for option in area_dropdown.options:
                self.assertTrue(option.text in areas_prefix)
                option.click()
                self.assertTrue(option.is_selected())

            self.logger.log(self.id(), 'Passed')
        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_area_dropdown')
            self.fail()

    @file_data('C:\Repos\Projects\SeleniumPOM\Tests\Data\data.json')
    def test_mobile_input(self, phone_number, **kwargs):
        """
        Name: Ros
        Function Name: test_mobile_input
        Description: testing input mobile field
        """

        mobile_regex = r'^\d{7}$'

        try:
            mobile_element = self.driver.find_element(*HPL.phone_locator)

            # Check if field is empty
            self.assertEqual(
                mobile_element.get_property('value'), "")

            # Valid input
            if (re.match(mobile_regex, phone_number)):
                mobile_element.send_keys(phone_number)
                # Assert field holding the value we inserted
                self.assertEqual(
                    mobile_element.get_property('value'), phone_number)
                # Assert name matches regex
                self.assertTrue(re.match(mobile_regex, phone_number))
                # Assert field property is valid
                self.assertTrue(
                    mobile_element.get_property("validity")["valid"])
                self.logger.log(self.id(), 'Passed')

            else:
                mobile_element.send_keys(phone_number)
                # Assert the valid property matches the incorrect mobile
                self.assertFalse(
                    mobile_element.get_property("validity")["valid"])
                self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_mobile_input')
            self.fail()

    def test_gender_radios(self):
        try:
            gender_radios = self.driver.find_elements(*HPL.genders_locator)

            for radio in gender_radios:
                radio.click()
                self.assertTrue(radio.is_selected())
                self.logger.log(self.id(), 'Passed')
        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_gender_radios')
            self.fail()

    def test_checkboxes(self):
        checkboxes_locators = [HPL.math_locator, HPL.physics_locator, HPL.pop_locator,
                               HPL.dud_locator, HPL.biology_locator, HPL.chem_locator, HPL.english_locator]

        try:
            for locator in checkboxes_locators:
                checkbox = self.driver.find_element(*locator)
                self.assertFalse(checkbox.is_selected())
                checkbox.click()
                self.assertTrue(checkbox.is_selected())

            self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_checkboxes')
            self.fail()

    @file_data('C:\Repos\Projects\SeleniumPOM\Tests\Data\data.json', 'positive_data')
    def test_clear(self, first_name, last_name, email, phone_number, **kwargs):
        input_locators = [HPL.firstname_locator,
                          HPL.lastname_locator, HPL.email_locator, HPL.phone_locator]
        click_locators = [HPL.city_locator, HPL.area_locator, HPL.male_locator, HPL.math_locator, HPL.physics_locator,
                          HPL.pop_locator, HPL.dud_locator, HPL.biology_locator, HPL.chem_locator, HPL.english_locator]

        input_locators_tuples = list(
            zip(input_locators, [first_name, last_name, email, phone_number]))

        try:
            for locator in input_locators_tuples:
                element = self.driver.find_element(*locator[0])
                # Check if field is empty
                self.assertEqual(element.get_property('value'), "")
                element.send_keys(locator[1])

            for locator in click_locators:
                element = self.driver.find_element(*locator)
                element.click()

            clear = self.driver.find_element(*HPL.clear_locator)
            clear.click()

            for input_locator, click_locator in zip(input_locators, click_locators):
                input_locator = self.driver.find_element(*input_locator)
                click_locator = self.driver.find_element(*click_locator)

                self.assertEqual(input_locator.get_property('value'), "")
                self.assertFalse(click_locator.is_selected())

            self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_clear')
            self.fail()

    @file_data('C:\Repos\Projects\SeleniumPOM\Tests\Data\data.json', 'positive_data')
    def test_send(self, first_name, last_name, email, phone_number, **kwargs):
        input_locators = [HPL.firstname_locator,
                          HPL.lastname_locator, HPL.email_locator, HPL.phone_locator]
        input_locators_tuples = list(
            zip(input_locators, [first_name, last_name, email, phone_number]))

        try:
            for locator in input_locators_tuples:
                element = self.driver.find_element(*locator[0])
                # Check if field is empty
                self.assertEqual(element.get_property('value'), "")
                element.send_keys(locator[1])

                send_element = self.driver.find_element(*HPL.send_locator)
                send_element.click()

            self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_send')
            self.fail()

    def test_set_text(self):
        try:
            set_text_button = self.driver.find_element(
                *HPL.setTextButton_locator)
            paragraph = self.driver.find_element(*HPL.setText_locator)
            actions = ActionChains(self.driver)

            self.assertTrue(not paragraph.text)
            actions.move_to_element(set_text_button).click().perform()
            alert = Alert(self.driver)
            alert.send_keys('`!24325asdgardREAGES*^%&@')
            alert.accept()
            self.assertEqual(paragraph.text, '`!24325asdgardREAGES*^%&@')
            self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_set_text')
            self.fail()

    def test_start_loading(self):
        try:
            startLoading_button = self.driver.find_element(
                *HPL.startLoadingButton_locator)
            paragraph = self.driver.find_element(*HPL.startLoading_locator)
            wait = WebDriverWait(self.driver, 10)

            self.assertEqual(paragraph.text, 'Click on Start Loading')
            startLoading_button.click()
            paragraph = wait.until(EC.text_to_be_present_in_element(
                HPL.startLoading_locator, 'Finish'))
            self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_start_loading')
            self.fail()

    def test_links(self):
        try:
            links = self.driver.find_elements(*HPL.links_locator)
            actions = ActionChains(self.driver)

            for link in links:
                if (link.text == 'Next Page'):
                    continue
                response = requests.get(link.get_attribute('href'))
                actions.key_down(Keys.CONTROL).click(
                    link).key_up(Keys.CONTROL).perform()
                self.driver.switch_to.window(self.driver.window_handles[-1])
                self.assertTrue(response.status_code == 200)

                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

            self.logger.log(self.id(), 'Passed')

        except Exception as e:
            self.logger.log(self.id(), f'Failed\n{e}')
            self.screenshoter.take_screenshot('test_links')
            self.fail()
