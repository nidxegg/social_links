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

Phone = '7776460761' #correct phone
email = 'luch_svet@mail.ru' #correct mail
name = 'Nick' #correct name

class TestProfile():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
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
  
  @pytest.mark.positive
  def test_profile(self):
    self.test_login()
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".userName").click()
    self.driver.find_element(By.LINK_TEXT, "Profile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".collapse:nth-child(6)").click()
    self.driver.find_element(By.ID, "profile-name").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, "profile-name").send_keys(name)
    self.driver.find_element(By.ID, "profile-email").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, "profile-email").send_keys(email)
    dropdown = self.driver.find_element(By.ID, "profile-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Kazakhstan']").click()
    self.driver.find_element(By.ID, "profile-country").click()
    self.driver.find_element(By.ID, "profile-phone").send_keys(Phone)
    dropdown = self.driver.find_element(By.ID, "profile-busseg")
    dropdown.find_element(By.XPATH, "//option[. = 'Police']").click()
    self.driver.find_element(By.ID, "profile-busseg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(7) > .btn:nth-child(1)").click()
    time.sleep(3)
    WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[5]/main/div[6]/section/form/div[6]/div/strong')), message='Регистрация не успешна')

  @pytest.mark.negative
  def test_empty_name(self):
    self.test_login()
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".userName").click()
    self.driver.find_element(By.LINK_TEXT, "Profile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".collapse:nth-child(6)").click()
    self.driver.find_element(By.ID, "profile-name").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, "profile-name").send_keys(" ")
    dropdown = self.driver.find_element(By.ID, "profile-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Kazakhstan']").click()
    self.driver.find_element(By.ID, "profile-phone").clear()
    self.driver.find_element(By.ID, "profile-phone").send_keys(Phone)

    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(7) > .btn:nth-child(1)").click()
    WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[5]/main/div[6]/section/form/div[6]/div/strong')), message='Пустое имя не прошло')

  @pytest.mark.negative
  def test_empty_phone(self):
    self.test_login()
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".userName").click()
    self.driver.find_element(By.LINK_TEXT, "Profile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".collapse:nth-child(6)").click()
    self.driver.find_element(By.ID, "profile-name").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, "profile-name").send_keys(name)
    self.driver.find_element(By.ID, "profile-email").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, "profile-email").send_keys(email)
    self.driver.find_element(By.ID, "profile-country").click()
    dropdown = self.driver.find_element(By.ID, "profile-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Kazakhstan']").click()
    self.driver.find_element(By.ID, "profile-country").click()
    self.driver.find_element(By.ID, "profile-phone").clear()
    self.driver.find_element(By.ID, "profile-phone").send_keys("")
    self.driver.find_element(By.ID, "profile-busseg").click()
    dropdown = self.driver.find_element(By.ID, "profile-busseg")
    dropdown.find_element(By.XPATH, "//option[. = 'Police']").click()
    self.driver.find_element(By.ID, "profile-busseg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(7) > .btn:nth-child(1)").click()
    time.sleep(3)
    WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[5]/main/div[6]/section/form/div[6]/div/strong')), message='Пустой телефон не прошел')

  @pytest.mark.negative
  def test_empty_email(self):
    self.test_login()
    self.driver.set_window_size(1607, 1027)
    self.driver.find_element(By.CSS_SELECTOR, ".userName").click()
    self.driver.find_element(By.LINK_TEXT, "Profile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".collapse:nth-child(6)").click()
    self.driver.find_element(By.ID, "profile-name").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, "profile-name").send_keys(name)
    self.driver.find_element(By.ID, "profile-email").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, "profile-email").send_keys(" ")
    self.driver.find_element(By.ID, "profile-phone").send_keys(Phone)
    dropdown = self.driver.find_element(By.ID, "profile-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Police']").click()
    self.driver.find_element(By.ID, "profile-phone").clear()
    self.driver.find_element(By.ID, "profile-phone").send_keys(Phone)

    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(7) > .btn:nth-child(1)").click()
    time.sleep(3)
    WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[5]/main/div[6]/section/form/div[6]/div/strong')), message='Пустая почта не прошла')
