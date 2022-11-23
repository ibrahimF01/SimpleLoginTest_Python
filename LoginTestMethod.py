from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # sayfa tam ekran
driver.implicitly_wait(30)


def loginTest(userName, password, posOrNeg):
    driver.get("https://demo.mersys.io/")
    driver.find_element(By.ID, "mat-input-0").send_keys(userName)
    driver.find_element(By.ID, "mat-input-1").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='LOGIN']").click()
    if (userName == "richfield.edu" and password == "ibrahimF") or (
            userName == "ibrahimF" and password == "Richfield2020!") and posOrNeg == "negative":
        invalidMessage = driver.find_element(By.CSS_SELECTOR, "dynamic-view[class='ng-star-inserted']>div").text
        return invalidMessage
    if (userName == "richfield.edu" and
        password == "Richfield2020!") and posOrNeg == "positive":
        dashboardVerify = driver.find_element(By.CSS_SELECTOR, "div[class='ng-star-inserted']>span").text
        return dashboardVerify

# Negative login test:
if "Invalid username or password" in loginTest("richfield.edu", "ibrahimF", "negative"):
    print("Negatif login test başarılı")
else:
    print("Negatif test başarısız")

#Pozitif login test:
if "Dashboard" in loginTest("richfield.edu", "Richfield2020!", "positive"):
    print("Pozitif login test başarılı")
else:
    print("Pozitif test başarısız")
