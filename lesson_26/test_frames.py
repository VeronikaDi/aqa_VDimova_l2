from assertpy import assert_that
import time


class TestFramesVerification:

    def test_frames_verification(self, browser):
        browser.get("http://localhost:8000/lesson_26/dz.html")

        browser.switch_to.frame("frame1")
        input1 = browser.find_element("id", "input1")
        input1.send_keys("Frame1_Secret")
        time.sleep(10)
        button1 = browser.find_element("tag name", "button")
        button1.click()
        time.sleep(10)
        alert1 = browser.switch_to.alert
        assert_that(alert1.text).is_equal_to("Верифікація пройшла успішно!")
        alert1.accept()
        browser.switch_to.default_content()

        browser.switch_to.frame("frame2")
        input2 = browser.find_element("id", "input2")
        input2.send_keys("Frame2_Secret")
        time.sleep(10)
        button2 = browser.find_element("tag name", "button")
        button2.click()
        time.sleep(10)
        alert2 = browser.switch_to.alert
        assert_that(alert2.text).is_equal_to("Верифікація пройшла успішно!")
        alert2.accept()
        browser.switch_to.default_content()
