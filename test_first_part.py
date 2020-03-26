from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

def test_case_1():
    driver = WebDriver(executable_path='C://bin//chromedriver.exe')
    driver.set_window_size(960, 1080)
    driver.get('https://qna.habr.com')
    search_input = driver.find_element_by_xpath('//input[@placeholder="Найти вопрос, ответ, тег или пользователя"]')
    search_input.send_keys('Selenium')
    driver.implicitly_wait(10)
    search_result = driver.find_element_by_xpath('//*[@id="ui-id-1"]')

    print(None)
    ...