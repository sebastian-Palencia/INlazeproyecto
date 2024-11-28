from data.config import settings 


class WebApp:

    def __init__(self, driver, evidence_path):
        self.driver = driver
        self.evidence_pathh = evidence_path
    
    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
                
        

