import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


url = "https://cringemdb.com/"


class SearchMovies(unittest.TestCase):

    def setUp(self, browser="ff"):
        if browser == "chrome" or browser == "ch":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_75/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        elif browser == "mozilla" or browser == "ff":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return self.driver


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


    def test_Search_Movies(self):
        searchMovies = self.driver.find_element_by_id("autocomplete")
        searchMovies.send_keys("Wrong Turn")
        searchMovie = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[starts-with(@id, 'ui-id-1')]//a[contains(text(),'Wrong Turn 2: Dead End (2007)')]")))
        searchMovie.click()
        print(self.driver.find_element_by_class_name("title").text)
        assert self.driver.find_element_by_class_name("title").text == "Wrong Turn 2: Dead End (2007)"





