from selenium import webdriver


browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title



# Selenium webdriver를 구동하여 실제로 크롬 브라우저를 띄운다.
# 로컬 컴퓨터에서 웹 페이지가 열리는지 확인한다.
# 열린 웹 페이지에서 Django 문자열이 있는지 확인한다