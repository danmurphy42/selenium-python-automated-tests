import os
from functools import wraps
from datetime import datetime


# decorator that takes a screenshot when tests fail. 
def capture_screenshot(function, driver_attr='driver'):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        try:
            function(self, *args, **kwargs)
        except Exception as e:
            driver = getattr(self, driver_attr)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            function_name = function.__name__
            if not os.path.exists('./tmp/screenshots'):
                os.makedirs('./tmp/screenshots')
            screenshot_path = "./tmp/screenshots" + f"/{function_name.split('test_')[1]}-{now}-failshot.png"
            driver.instance.save_screenshot(screenshot_path)
            raise e
    return wrapper
