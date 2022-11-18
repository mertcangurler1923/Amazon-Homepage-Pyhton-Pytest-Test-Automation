import pytest
from pages.AmazonHomepagePage import AmazonHomepagePage

@pytest.mark.usefixtures("setUp")
class TestAmazonHomepage():
    def test_signIn(self):
        amazonHomepagePage = AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.signInControl()
        assert location != "https://www.amazon.com.tr/"

    def test_controlBoxesPicturesAndTexts(self):
        amazonHomepagePage = AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.controlBoxesPicturesAndTexts()
        for i in location:
            for k in i:
                assert k != "https://www.amazon.com.tr/"

    def test_homeCoverPhotoChangeClickAndPhoto(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.homeCoverPhotoChangeClickAndPhotoControl()
        for i in location:
            assert i != "https://www.amazon.com.tr/"

    def test_list1(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.listControl1()
        for i in location:
            assert i != "https://www.amazon.com.tr/"

    def test_list2(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.listControl2()
        for i in location:
            assert i != "https://www.amazon.com.tr/"

    def test_list3(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.listControl3()
        for i in location:
            assert i != "https://www.amazon.com.tr/"

    def test_list4(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.listControl4()
        for i in location:
            assert i != "https://www.amazon.com.tr/"

    def test_list5(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.listControl5()
        for i in location:
            assert i != "https://www.amazon.com.tr/"

    def test_list6(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.listControl6()
        for i in location:
            assert i != "https://www.amazon.com.tr/"

    def test_list7(self):
        amazonHomepagePage=AmazonHomepagePage(self.driver)
        location = amazonHomepagePage.listControl7()
        for i in location:
            assert i != "https://www.amazon.com.tr/"
