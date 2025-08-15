import pytest
import configparser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from faker import Faker
import random
import os
from pages.broken_links_page import BrokenLinksPage
from pages.browser_windows_page import BrowserWindowsPage
from pages.buttons_page import ButtonsPage
from pages.check_box_page import CheckBoxPage
from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.links_page import LinksPage
from pages.radio_button_page import RadioButtonPage
from pages.text_box_page import TextBoxPage
from pages.upload_download_page import UploadDownloadPage
from pages.web_tables_page import WebTablesPage
from pages.practice_form_page import PracticeFormPage


@pytest.fixture(scope="session")
def config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@pytest.fixture(scope="function")
def driver(config):
    # Get the project's root directory
    project_root = os.getcwd()
    download_dir = os.path.join(project_root, "downloads")

    # Ensure the download directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    base_url = config["DEMOQA"]["BASE_URL"]
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Configure Chrome to automatically save downloads to the specified directory
    prefs = {"download.default_directory": download_dir,
             "download.prompt_for_download": False}  # Prevents download dialog pop-up
    chrome_options.add_experimental_option("prefs", prefs)

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
def web_tables_page(driver, config) -> WebTablesPage:
    """
    Fixture that returns a WebTablesPage object and navigates to its URL.
    """
    web_tables_page = WebTablesPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    web_tables_page.open_url(f"{base_url}/{config['DEMOQA']['WEBTABLES_URL']}")
    return web_tables_page


@pytest.fixture(scope="function")
def buttons_page(driver, config):
    """
    Fixture that returns a ButtonsPage object and navigates to its URL.
    """
    buttons_page = ButtonsPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    buttons_page.open_url(f"{base_url}/{config['DEMOQA']['BUTTONS_URL']}")
    return buttons_page


@pytest.fixture(scope="function")
def links_page(driver, config):
    """
    Fixture that returns a LinksPage object and navigates to its URL.
    """
    links_page = LinksPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    links_page.open_url(f"{base_url}/{config['DEMOQA']['LINKS_URL']}")
    return links_page


@pytest.fixture(scope="function")
def broken_links_page(driver, config):
    """
    Fixture that returns a BrokenLinksPage object and navigates to its URL.
    """
    broken_links_page = BrokenLinksPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    broken_links_page.open_url(f"{base_url}/{config['DEMOQA']['BROKEN_LINKS_URL']}")
    return broken_links_page


@pytest.fixture(scope="function")
def upload_download_page(driver, config):
    """
    Fixture that returns an UploadDownloadPage object and navigates to its URL.
    """
    upload_download_page = UploadDownloadPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    upload_download_page.open_url(f"{base_url}/{config['DEMOQA']['UPLOAD_DOWNLOAD_URL']}")
    return upload_download_page


@pytest.fixture(scope="function")
def dynamic_properties_page(driver, config):
    """
    Fixture that returns a DynamicPropertiesPage object and navigates to its URL.
    """
    dynamic_properties_page = DynamicPropertiesPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    dynamic_properties_page.open_url(f"{base_url}/{config['DEMOQA']['DYNAMIC_PROPERTIES_URL']}")
    return dynamic_properties_page


@pytest.fixture(scope="function")
def practice_form_page(driver, config):  # Added new fixture
    """
    Fixture that returns a PracticeFormPage object and navigates to its URL.
    """
    practice_form_page = PracticeFormPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    practice_form_page.open_url(f"{base_url}/{config['DEMOQA']['PRACTICE_FORM_URL']}")
    return practice_form_page


@pytest.fixture(scope="function")
def browser_windows_page(driver, config):
    """
    Fixture that returns a BrowserWindowsPage object and navigates to its URL.
    """
    browser_windows_page = BrowserWindowsPage(driver)
    base_url = config['DEMOQA']['BASE_URL']
    browser_windows_page.open_url(f"{base_url}/{config['DEMOQA']['BROWSER_WINDOWS_URL']}")
    return browser_windows_page


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


@pytest.fixture(scope="function")
def web_tables_test_data():
    """
    Fixture that generates fake data using the Faker library for the Web Tables tests.
    """
    fake = Faker()
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": str(fake.random_int(min=18, max=65)),
        "salary": str(fake.random_int(min=30000, max=150000)),
        "department": fake.job()
    }


@pytest.fixture(scope="function")
def generated_form_data():
    """
    Generates a dictionary of random test data using the Faker library.
    This fixture ensures a new set of data for each test run.
    """
    fake = Faker()
    # A list of possible subjects and hobbies to choose from
    subjects_list = ["Maths", "Computer Science", "Physics", "English", "History", "Chemistry", "Social Studies"]
    hobbies_list = ["Sports", "Reading", "Music"]

    # A dictionary to map states to cities for dynamic selection
    state_city_mapping = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }

    # Randomly select a state and a corresponding city
    random_state = random.choice(list(state_city_mapping.keys()))
    random_city = random.choice(state_city_mapping[random_state])

    # Randomly select a few items for subjects and hobbies
    num_subjects = random.randint(1, 3)
    selected_subjects = random.sample(subjects_list, num_subjects)
    selected_hobbies = random.sample(hobbies_list, random.randint(1, len(hobbies_list)))
    selected_hobbies.sort()

    file_path = os.path.join(os.path.dirname(__file__), '..', 'sample_picture.png')
    file_to_upload = file_path if os.path.exists(file_path) else None
    if not file_to_upload:
        print(f"\nWarning: The file '{file_path}' does not exist. Skipping picture upload.")

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "gender": random.choice(["Male", "Female", "Other"]),
        "mobile_number": fake.numerify("##########"),  # Generates a 10-digit number
        "day_of_birth": str(random.randint(10, 28)),
        "month_of_birth": random.choice(["January", "February", "March", "April", "May", "June",
                                         "July", "August", "September", "October", "November", "December"]),
        "year_of_birth": str(random.randint(1950, 2000)),
        "subjects": selected_subjects,
        "hobbies": selected_hobbies,
        "address": fake.address().replace("\n", " "),  # Removes newlines for the input field
        "state": random_state,
        "city": random_city,
        "file_to_upload": file_to_upload
    }