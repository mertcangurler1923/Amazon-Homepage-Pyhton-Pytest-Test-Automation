from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.BaseFunctions import BaseFunctions

class AmazonHomepagePage(BaseFunctions):

    cookie = (By.CSS_SELECTOR, "input[id='sp-cc-accept']")

    signUp = (By.CSS_SELECTOR, "a[class*='a-button-text']")

    photoButtons = (By.CSS_SELECTOR, "div[cel_widget_id*='gw-desktop-hero-'] i[class*='a-icon a-icon-']")

    photoClickButton = (By.CSS_SELECTOR, "div[class='a-row a-carousel-controls a-carousel-row a-carousel-has-buttons a-carousel-overlay-buttons a-carousel-rounded-buttons']")

    photoCard = (By.CSS_SELECTOR, "div[class='a-carousel-viewport'] li[class='a-carousel-card']  img[alt]")

    photoValue = (By.CSS_SELECTOR, "input[class='a-carousel-firstvisibleitem']")

    texts = (By.CSS_SELECTOR, "a[class='a-link-normal see-more truncate-1line']")

    images = (By.CSS_SELECTOR, "div[class='a-section a-spacing-none fluid-image-container']")

    list1Buttons = (By.CSS_SELECTOR, "div[id='desktop-1'] a[aria-label*='Carousel']")

    list1Card = (By.CSS_SELECTOR, "div[id='desktop-1'] li[class*='feed-carousel-card']")

    list2Buttons = (By.CSS_SELECTOR, "div[id='desktop-2'] a[aria-label]")

    list2Card = (By.CSS_SELECTOR, "div[id='desktop-2'] li[class*='feed-carousel-card']")

    list3Buttons = (By.CSS_SELECTOR, "div[id='desktop-3'] a[aria-label*='Carousel']")

    list3Card = (By.CSS_SELECTOR, "div[id='desktop-3'] li[class*='feed-carousel-card']")

    list4Buttons = (By.CSS_SELECTOR, "div[id='desktop-4'] a[aria-label]")

    list4Card = (By.CSS_SELECTOR, "div[id='desktop-4'] li[class*='feed-carousel-card']")

    list5Buttons = (By.CSS_SELECTOR, "div[id='desktop-5'] a[aria-label*='Carousel']")

    list5Card = (By.CSS_SELECTOR, "div[id='desktop-5'] li[class*='feed-carousel-card']")

    list6Buttons = (By.CSS_SELECTOR, "div[id='desktop-6'] a[aria-label]")

    list6Card = (By.CSS_SELECTOR, "div[id='desktop-6'] li[class*='feed-carousel-card']")

    list7Buttons = (By.CSS_SELECTOR, "div[id='desktop-7'] a[aria-label*='Carousel']")

    list7Card = (By.CSS_SELECTOR, "div[id='desktop-7'] li[class*='feed-carousel-card']")

    def __init__(self, driver):
        super().__init__(driver)

    def signInControl(self):
        self.beAUser(self.cookie)
        self.click(self.signUp)
        location = self.driver.current_url
        return location

    def controlBoxesPicturesAndTexts(self):
        textsLocation = self.boxElementControl(self.cookie, self.texts)
        imagesLocation = self.boxElementControl(self.cookie, self.images)
        location = [textsLocation, imagesLocation]
        return location

    def homeCoverPhotoChangeClickAndPhotoControl(self):
        self.beAUser(self.cookie)
        buttonsList = self.findAll(self.photoButtons)
        cardList = self.findAll(self.photoCard)
        location = []
        for a in range(0, len(buttonsList), 1):
            for i in range(1, len(cardList), 1):
                count = True
                while count == True:
                    self.beAUser(self.cookie)
                    value = self.getattribute(self.photoValue, "value")
                    c = self.find((By.CSS_SELECTOR, "[name='field-keywords']"))
                    c.send_keys(str(i)+":"+str(value)+",")
                    c.send_keys(Keys.ESCAPE)
                    if int(value) == i:
                        self.click(self.photoClickButton)
                        getlocation = self.driver.current_url
                        location.append(getlocation)
                        self.driver.back()
                        count = False
                    else:
                        buttonsList = self.findAll(self.photoButtons)
                        self.clickElement(buttonsList[a])
        return location

    def listControl1(self):
        location = self.listControl(self.cookie, self.list1Buttons, self.list1Card)
        return location

    def listControl2(self):
        location = self.listControl(self.cookie, self.list2Buttons, self.list2Card)
        return location

    def listControl3(self):
        location = self.listControl(self.cookie, self.list3Buttons, self.list3Card)
        return location

    def listControl4(self):
        location = self.listControl(self.cookie, self.list4Buttons, self.list4Card)
        return location

    def listControl5(self):
        location = self.listControl(self.cookie, self.list5Buttons, self.list5Card)
        return location

    def listControl6(self):
        location = self.listControl(self.cookie, self.list6Buttons, self.list6Card)
        return location

    def listControl7(self):
        location = self.listControl(self.cookie, self.list7Buttons, self.list7Card)
        return location


