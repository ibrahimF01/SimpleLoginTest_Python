from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # sayfa tam ekran
driver.implicitly_wait(30)

#Doğru kullanıcı adı ve yanlış şifre ile negatif login testi
driver.get("https://demo.mersys.io/")
print("Girilen website: "+driver.title)
userNameInput=driver.find_element(By.ID, "mat-input-0")
userNameInput.send_keys("richfield.edu")
passwordInput=driver.find_element(By.ID, "mat-input-1")
passwordInput.send_keys("ibrahimF")
loginButton=driver.find_element(By.CSS_SELECTOR, "button[aria-label='LOGIN']")
loginButton.click()
invalidMessage=driver.find_element(By.CSS_SELECTOR, "dynamic-view[class='ng-star-inserted']>div").text
print("Invalid Message: "+invalidMessage)
if "Invalid username or password" in invalidMessage: print("Negatif login test(hatalı şifre ile) başarılı")
else: print("Negatif test başarısız")

#Yanlış kullanıcı adı ve doğru şifre ile negatif login testi
driver.get("https://demo.mersys.io/")
print("Girilen website: "+driver.title)
userNameInput=driver.find_element(By.ID, "mat-input-0")
userNameInput.send_keys("ibrahimF")
passwordInput=driver.find_element(By.ID, "mat-input-1")
passwordInput.send_keys("Richfield2020!")
loginButton=driver.find_element(By.CSS_SELECTOR, "button[aria-label='LOGIN']")
loginButton.click()
invalidMessage=driver.find_element(By.CSS_SELECTOR, "dynamic-view[class='ng-star-inserted']>div").text
print("Invalid Message: "+invalidMessage)
if "Invalid username or password" in invalidMessage: print("Negatif login test(hatalı kullanıcı adı ile) başarılı")
else: print("Negatif test başarısız")

#Doğru kullanıcı adı ve doğru şifre ile pozitif login testi
driver.get("https://demo.mersys.io/")
print("Girilen website: "+driver.title)
userNameInput=driver.find_element(By.ID, "mat-input-0")
userNameInput.send_keys("richfield.edu")
passwordInput=driver.find_element(By.ID, "mat-input-1")
passwordInput.send_keys("Richfield2020!")
loginButton=driver.find_element(By.CSS_SELECTOR, "button[aria-label='LOGIN']")
loginButton.click()
dashboardVerify=driver.find_element(By.CSS_SELECTOR, "div[class='ng-star-inserted']>span").text
print("Dashboard doğrulama: "+dashboardVerify)
if "Dashboard" in dashboardVerify: print("Pozitif login test(Doğru kullanıcı adı ve şifre ile) başarılı")
else: print("Pozitif test başarısız")

driver.quit()
