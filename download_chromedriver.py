import requests
import shutil
import os
from pathlib import Path
from subprocess import run
from subprocess import DEVNULL


class DownloadChromedriver:
    def __init__(self, chromedriver_version):
        self.current_path = str(Path(__file__).parent)
        self.zipped_chromedriver_path = self.current_path + '/chromedriver/chromedriver.zip'
        self.unzipped_chromedriver_path = self.current_path + '/chromedriver-linux64/chromedriver'
        self.chromedriver_download_page = (("https://storage.googleapis.com/"
                                            "chrome-for-testing-public/{}/linux64/chromedriver-linux64.zip")
                                           .format(chromedriver_version))
        self.version = chromedriver_version
        self.get_request = requests.get(self.chromedriver_download_page)

    def start(self):
        print("\nDownloading Chromedriver version {}".format(self.version))
        while True:
            try:
                with open(self.zipped_chromedriver_path, 'wb') as dl_chromedriver:
                    dl_chromedriver.write(self.get_request.content)
                dl_chromedriver.close()
                break
            except FileNotFoundError:
                os.mkdir(self.current_path + '/chromedriver/')

    def file_operations(self):
        unzip_command = ['unzip', self.zipped_chromedriver_path]
        move_the_zip_file = ['mv', self.unzipped_chromedriver_path, self.current_path + '/chromedriver/']
        run(unzip_command, shell=False, stdout=DEVNULL)
        run(move_the_zip_file, shell=False, stdout=DEVNULL)
        shutil.rmtree(self.current_path + '/chromedriver-linux64/')
        os.remove(self.zipped_chromedriver_path)
        input("Done. Press Enter to return to menu")
