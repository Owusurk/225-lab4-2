import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class TestContacts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Allow override via environment variable, default to your Dev IP
        cls.base_url = os.environ.get("DEV_URL", "http://10.48.229.143")

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        cls.driver = webdriver.Firefox(options=options)

    def test_contacts_present(self):
        driver = self.driver
        driver.get(self.base_url)

        # Give the app a little time to render and pull data
        time.sleep(5)

        page = driver.page_source

        # Check for the presence of all 10 test contacts
        for i in range(10):
            test_name = f"Test Name {i}"
            self.assertIn(
                test_name,
                page,
                msg=f"Test contact {test_name} not found in page source",
            )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
