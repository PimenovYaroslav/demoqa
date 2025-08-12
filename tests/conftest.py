import pytest
import configparser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.elements_page import ElementsPage
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@pytest.fixture(scope="function")
def driver(config):
    base_url = config["DEMOQA"]["BASE_URL"]
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = ChromeService(ChromeDriverManager().install())

    try:
        service = ChromeService(ChromeDriverManager().install())
    except Exception as e:
        pytest.fail(f"Failed to install ChromeDriver: {e}")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(base_url)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def home_page(driver, config) -> HomePage:
    """
    Fixture to create and return a HomePage object, and open the homepage URL.
    """
    home_page = HomePage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    home_page.open_url(base_url)
    return home_page


@pytest.fixture(scope="function")
def elements_page(driver, config) -> ElementsPage:
    """
    Fixture to create and return an ElementsPage object, and navigate directly to its URL.
    """
    elements_page = ElementsPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    elements_page.open_url(f"{base_url}/{config['DEMOQA']['ELEMENTS_URL']}")
    return elements_page
