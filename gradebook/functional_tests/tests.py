from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)



class NewVisitorTest(LiveServerTestCase):        
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.close()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url+'/grades/')
        self.browser.save_screenshot('test.png')
        self.assertEqual(1+1,3)
