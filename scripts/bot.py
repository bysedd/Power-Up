from pathlib import Path

import geckodriver_autoinstaller as geckodriver
from selenium import webdriver

from scripts.utils import Utils


class Bot:
    """
    This class is responsible for interacting with the web page,
    writing the products from the file to the form, and closing the browser.
    """

    URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/tabela"
    FILE_PATH = Path(__file__).parent.parent / "resources" / "produtos.csv"

    def __init__(self):
        """
        Installs the geckodriver if necessary and initializes the elements.
        """
        self._install_driver()
        self._initialize_elements()

    def _install_driver(self):
        """
        Installs the geckodriver if it is not already installed.
        """
        if geckodriver.get_firefox_version() is None:
            geckodriver.install()
        self.driver = webdriver.Firefox()

    def _initialize_elements(self):
        """
        Reads the products from the file, gets the header and mounts the elements.
        """
        self.products = Utils.read_file(self.FILE_PATH)
        self.header = self.products.pop(0).split(",")
        self.elements = Utils.mount_elements(self.header)
        self.elements["submit"] = 'button[type="submit"]'

    def open_site(self):
        """
        Opens the site.
        """
        self.driver.get(self.URL)

    def write_product(self, product: str):
        """
        Writes a product to the form.

        Args:
            product (str): The product to be written.
        """
        split_product = product.split(",")
        for column_name, selector in self.elements.items():
            element = self.driver.find_element(value=selector)
            element.send_keys(split_product[self.header.index(column_name)])
        self.driver.find_element(by="css selector", value=self.elements["submit"]).click()

    def write(self):
        """
        Writes all products to the form.
        """
        for product in self.products:
            self.write_product(product)

    def run(self):
        """
        Opens the site and writes all products.
        """
        self.open_site()
        self.write()

    def __del__(self):
        """
        Closes the browser.
        """
        input("Press Enter to close the browser...")
        self.driver.close()
