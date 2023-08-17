from selenium import webdriver


class Browser:
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.maximize_window()

    def close(self):
        self.browser.close()
