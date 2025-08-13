import pytest
import configparser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from faker import Faker

from pages.check_box_page import CheckBoxPage
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.radio_button_page import RadioButtonPage
from pages.text_box_page import TextBoxPage


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


@pytest.fixture(scope="function")
def text_box_page(driver, config) -> TextBoxPage:
    """
    Fixture to create and return an TextBoxPage object, and navigate directly to its URL.
    """
    textbox_page = TextBoxPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    textbox_page.open_url(f"{base_url}/{config['DEMOQA']['TEXTBOX_URL']}")
    return textbox_page


@pytest.fixture(scope="function")
def check_box_page(driver, config) -> CheckBoxPage:
    """
    Fixture to create and return a CheckBoxPage object, and navigate directly to its URL.
    """
    check_box_page = CheckBoxPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    check_box_page.open_url(f"{base_url}/{config['DEMOQA']['CHECKBOX_URL']}")
    return check_box_page


@pytest.fixture(scope="function")
def radio_button_page(driver, config) -> RadioButtonPage:
    """
    Fixture that returns a RadioButtonPage object and navigates to its URL.
    """
    radio_button_page = RadioButtonPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    radio_button_page.open_url(f"{base_url}/{config['DEMOQA']['RADIO_BUTTON_URL']}")
    return radio_button_page


@pytest.fixture(scope="function")
def test_data():
    """
    Fixture that generates fake data using the Faker library.
    NOTE: You need to install Faker first: pip install Faker
    """
    fake = Faker()
    return {
        "full_name": fake.name(),
        "email": fake.email(),
        "current_address": fake.address(),
        "permanent_address": fake.address()
    }
