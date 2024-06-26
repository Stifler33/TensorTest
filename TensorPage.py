from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import logging


class Stage_1(BasePage):

    def click_banner_tensor(self):
        original_window = self.driver.current_window_handle
        try:
            self.find_element(By.XPATH, "//*[@id='contacts_clients']/div[1]/div/div/div[2]/div/a/img").click()
            time.sleep(1)
            for window in self.driver.window_handles:
                if window != original_window:
                    self.driver.switch_to.window(window)
                    logging.info(f"switch to new window !\nnew url : {self.driver.current_url}")
            return self.driver.current_url
        except EC.NoSuchElementException:
            logging.warning("exception No Such Element Exception")
        except EC.StaleElementReferenceException:
            logging.warning("exception Stale Element Reference Exception")

    def check_power_in_human(self):
        powerInHuman = None
        try:
            time.sleep(1)
            logging.info(f"start search block power in human\nurl : {self.driver.current_url}")
            blockHuman = self.find_element(By.CLASS_NAME, "tensor_ru-Index__block4-content")
            elements = blockHuman.find_elements(By.TAG_NAME, "p")
            for element in elements:
                if element.text == "Сила в людях":
                    powerInHuman = element
            if powerInHuman is None:
                logging.error("banner is not found")
            else:
                logging.info(f"banner power in human found '{powerInHuman.text}'")
            return powerInHuman
        except EC.NoSuchElementException:
            logging.warning("power in human is not found")
            return None

    def open_power_in_human_about(self):
        try:
            about = self.find_element(By.XPATH,
                                      "//*[@id='container']/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a").get_attribute(
                "href")
            self.driver.get(about)
            logging.info("success click about")
            return self.driver.current_url
        except EC.NoSuchElementException:
            logging.warning("error click about. exception NoSuchElementException")
            return ""
        except EC.StaleElementReferenceException:
            logging.warning("exception StaleElementReferenceException")
            return ""

    def check_block_work_h_w(self):
        listImage = ["//*[@id='container']/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img",
                     "//*[@id='container']/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img",
                     "//*[@id='container']/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img",
                     "//*[@id='container']/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img"]
        listHeight = [self.find_element(By.XPATH, img).rect["height"] for img in listImage]
        listWidth = [self.find_element(By.XPATH, img).rect["width"] for img in listImage]
        if len(set(listHeight)) != 1 and len(set(listWidth)) != 1:
            return False
        return True


class Stage_2(BasePage):

    def check_region(self, region):
        current_region = self.find_element(By.XPATH,
                                           "//*[@id='container']/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span").text
        if current_region == region:
            return True
        else:
            return False

    def check_list_partner(self):
        try:
            time.sleep(1)
            list_partner = [partner.text for partner in self.find_elements(By.CLASS_NAME, "sbisru-Contacts-List__name")]
            logging.info(f"list partner : {list_partner}")
            return list_partner
        except EC.StaleElementReferenceException:
            logging.info("received StaleElementReferenceException")
            return []

    def edit_region(self):
        time.sleep(0.5)
        self.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser__text").click()
        time.sleep(0.5)
        self.find_element(By.XPATH, "//*[@id='popup']/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span").click()

    def check_url_title_41(self):
        title = "Камчатский край"
        url = "41-kamchatskij-kraj"
        return self.driver.current_url.find(url) != -1 and self.driver.title.find(title) != -1
