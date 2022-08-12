from selenium import webdriver


browser = webdriver.Firefox()
browser.get('localhost:8000')

assert 'successfully' in browser.title








