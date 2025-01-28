
import time
import io

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image


class Screenshotter:

    def __init__(self, websites, output_path):
        self.websites = websites
        self.output_path = output_path
        self.current_index = 0

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.capture_screenshots()

    def capture_screenshots(self):

        for website in self.websites:
            url = website["web"]
            entry_id = website["id"]
            print(f"Loading: {url}")

            self.driver.get(url)
            time.sleep(2)  # Wait for page to load

            screenshot = self.driver.get_screenshot_as_png()
            image = Image.open(io.BytesIO(screenshot))

            filename = f"{self.output_path}{entry_id}.png"
            image.save(filename, "PNG")

            print(f"Screenshot saved at: {filename}")

            time.sleep(1)

        print("All screenshots completed.")
        self.driver.quit()


websites = [
    { "id": "richardreinisch", "web": "https://richardreinisch.com" },
    { "id": "energiezentren", "web": "https://www.energiezentren.com" },
    { "id": "drachenzahm", "web": "https://www.drachenzahm.com" }
]

output_path = "./data/"

screenshotter = Screenshotter(websites, output_path)

