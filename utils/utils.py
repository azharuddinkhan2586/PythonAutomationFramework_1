import inspect
import allure
import moment

def currenttestname():
    return inspect.stack()[1][3]


def capturescreenshot(driver,testname):
    currtime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
    screenshotname = testname + "_" + currtime
    allure.attach(driver.get_screenshot_as_png(), name=screenshotname, attachment_type=allure.attachment_type.PNG)