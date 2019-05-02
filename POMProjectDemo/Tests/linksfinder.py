from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Allah/Desktop/Pythan/Projects/FirstSeleniumTest/Drivers/chromedriver.exe')
driver.get("http://www.inmar.com")
driver.maximize_window()
driver.implicitly_wait(10)
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    # Displaying all the links on web page
    print elem.get_attribute("href")
    print elem.get_attribute("text")
    # print elem.get_attribute("html tag")
print "Done"
driver.close()
driver.quit()
