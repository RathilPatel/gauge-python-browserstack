from getgauge.python import before_step, after_step, before_scenario, after_scenario, before_spec, after_spec, before_suite, after_suite,step
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os,time
import step_impl.driver_setup

browser= None
@before_spec
def init():
    global browser
    browser = step_impl.driver_setup.driverinit()
@step("Goto <url>")
def URL_visit(word):
    global browser
    browser.get(word)
@step("Field name <q> Enter text <textvalue>")
def text_enter(field,textvalue):
    global browser
    elem = browser.find_element_by_name(field)
    elem.send_keys(textvalue)
    elem.submit()
@step("Page title")
def get_title():
    global browser
    print (browser.title)
    
    


