from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class BaseFunctions:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(driver, 2)

    def find(self, locator):
        # element = self.driver.find_element(*locator)
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def findAll(self, locator):
        count = True
        while count == True:
            list = self.driver.find_elements(*locator)
            if len(list) > 0:
                count = False
        return list

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def clickElement(self, element):
        element.click()

    def wait(self, element):
        self.wait.until(EC.visibility_of(element))

    def getattribute(self, locator, attribute):
        count = True
        while count == True:
            value = self.driver.find_element(By.CSS_SELECTOR, "input[class='a-carousel-firstvisibleitem']").get_attribute("value")
            if value != "":
                count = False
        return value

    def scrollToPageFind(self, element):
        count = True

        while count == True:
            sleep(10)
            try:
                self.wait().until(EC.element_to_be_clickable(element))
                count = False
            except:
                self.driver.execute_script("window.scrollBy(0," + str(700) + ")")
                sleep(1)

    def scrollToElement(self, web_element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})", web_element)
        sleep(1)

    def moveToElement(self, element):
        self.actions.move_to_element(element).perform()

    def beAUser(self, locator):
        try:
            self.click(locator)
        except:
            i=0

    def listControl(self, cookie, buttons, cards):
        self.beAUser(cookie)
        buttonsList = self.findAll(buttons)
        cardList = self.findAll(cards)
        self.scrollToElement(cardList[0])
        location = []
        for i in range(0, len(cardList), 1):
            count = True
            while count == True:
                try:
                    cardList = self.findAll(cards)
                    self.beAUser(cookie)
                    self.scrollToElement(cardList[i])
                    self.clickElement(cardList[i])
                    getlocation = self.driver.current_url
                    location.append(getlocation)
                    self.driver.back()
                    count = False
                except:
                    buttonsList = self.findAll(buttons)
                    cardList = self.findAll(cards)
                    self.scrollToElement(cardList[i])
                    self.moveToElement(cardList[i])
                    self.clickElement(buttonsList.get(1))
        for i in range(1, -1, -1):
            cardList = self.findAll(cards)
            self.beAUser(cookie)
            sleep(2)
            self.scrollToElement(cardList[i])
            buttonsList = self.findAll(buttons)
            if i == 1:
                self.moveToElement(cardList[i])
            for a in range(0, 3, 1):
                self.clickElement(buttonsList[i])
                sleep(1)
        return location

    def boxElementControl(self, cookie, card):
        self.beAUser(cookie)
        cardList = self.findAll(card)
        location = []
        for i in range(1, len(cardList), 1):
            self.beAUser(self.cookie)
            cardList = self.findAll(card)
            self.scrollToElement(cardList[i])
            self.clickElement(cardList[i])
            getlocation = self.driver.current_url
            location.append(getlocation)
            self.driver.back()
        return location

