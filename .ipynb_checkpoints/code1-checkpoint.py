from selenium import webdriver

path = "Download\chromedriver_win32\chromedriver.exe" # 상대경로로 입력

driver = webdriver.Chrome(path)

driver.get('https://www.google.co.kr')