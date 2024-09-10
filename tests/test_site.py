import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')


def test_two_monitors(driver):
    # driver.get('https://www.demoblaze.com/index.html')
    homepage = HomePage(driver)
    homepage.open()
    # monotor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    # monotor_link.click()
    homepage.click_monitor()
    time.sleep(2)
    # monitors = driver.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 2
    homepage.check_products_count(2)
