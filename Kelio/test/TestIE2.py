from selenium import webdriver


class test_Navigateur_Defaut(object):
    """
        test_Navigateur_Defaut framework are committed to a simpler automated testing,
    based on the original selenium.
    """

    def __init__(self, browser='firefox'):
        """
        Run class initialization method, the default is proper
        to drive the Firefox browser,. Of course, you can also
        pass parameter for other browser, such as Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        """
        if browser == "firefox" :
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "ie" :
            driver = webdriver.Ie()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie'.")


driver = test_Navigateur_Defaut('ie')