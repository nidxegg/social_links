import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC   

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  @pytest.mark.positive
  def test_login(self):
    self.driver.get("https://area.mtg-bi.com/")
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".sign-page").click()
    self.driver.find_element(By.LINK_TEXT, "Sign IN").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "signin-login").send_keys("testcaseqa5@gmail.com")
    self.driver.find_element(By.ID, "signin-pass").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > .btn").click()
    time.sleep(3)
    expectedUrl =  self.driver.current_url
    assert  expectedUrl == 'https://area.mtg-bi.com/main', 'Вход не удался'
 
  @pytest.mark.negative
  def test_empty_fields(self):
    self.driver.get("https://area.mtg-bi.com/")
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".sign-page").click()
    self.driver.find_element(By.LINK_TEXT, "Sign IN").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "signin-login").send_keys("")
    self.driver.find_element(By.ID, "signin-pass").send_keys("")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > .btn").click()
    time.sleep(3)
    expectedUrl =  self.driver.current_url
    assert  expectedUrl == 'https://area.mtg-bi.com/main', 'Пустые поля не прошли'
  
  @pytest.mark.negative
  def test_empty_mail(self):
    self.driver.get("https://area.mtg-bi.com/")
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".sign-page").click()
    self.driver.find_element(By.LINK_TEXT, "Sign IN").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "signin-login").send_keys("")
    self.driver.find_element(By.ID, "signin-pass").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > .btn").click()
    time.sleep(3)
    expectedUrl =  self.driver.current_url
    assert  expectedUrl == 'https://area.mtg-bi.com/main', 'Пустая почта не прошла'

  @pytest.mark.negative
  def test_empty_pass(self):
    self.driver.get("https://area.mtg-bi.com/")
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".sign-page").click()
    self.driver.find_element(By.LINK_TEXT, "Sign IN").click()
    time.sleep(3)
    self.driver.find_element(By.ID, "signin-login").send_keys("testcaseqa5@gmail.com")
    self.driver.find_element(By.ID, "signin-pass").send_keys("")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > .btn").click()
    time.sleep(3)
    expectedUrl =  self.driver.current_url
    assert  expectedUrl == 'https://area.mtg-bi.com/main', 'Пустой пароль не прошел'
