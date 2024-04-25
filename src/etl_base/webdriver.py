from selenium.webdriver import Chrome, ChromeOptions


class Webdriver(Chrome):
    def __init__(self, headless: bool = True) -> None:
        opts = ChromeOptions()
        if headless:
            opts.add_argument('--headless')
        super().__init__(options=opts)
