from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        #self.logger = logger
        self.base_url = "https://sbis.ru/"
        driver.implicitly_wait(5)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_Contacts(self):
        contacts = self.find_element(By.LINK_TEXT, "Контакты")
        contacts.click()
        return contacts

