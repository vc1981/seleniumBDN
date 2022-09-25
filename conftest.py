import pytest
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setup(request):
    # display = Display(size=(1920, 1200), color_depth=24, backend="xvfb")
    # display.start()

    chrome_options = Options()
    options = [
        #"--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ingnore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-infobars",
        "--dns-prefetech-disable",
        "--disable-features=VizDisplayCompositor"
    ]

    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()
    # display.stop()