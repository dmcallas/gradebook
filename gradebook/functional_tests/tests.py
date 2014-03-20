from django.test import TestCase, LiveServerTestCase
from grades import models
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
        department=models.Department(name='MATH',long_name='Mathematics')
        department.save()
        course=models.Course(title='Math 100',number='100',department=department)
        course.save()
        semester=models.Semester(name='Fall',year=2014)
        semester.save()
        models.Section(course=course,number=1234,semester=semester).save()
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.close()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url+'/grades/')
        self.browser.save_screenshot('test1.png')
        self.browser.find_element_by_id('section-1-link').click()
        self.browser.save_screenshot('test2.png')
        # Check menus...
        #self.browser.
        self.assertEqual(1+1,3)


