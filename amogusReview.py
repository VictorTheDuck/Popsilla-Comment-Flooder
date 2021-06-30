from selenium import webdriver
import random
import time
message = input('What would you like to flood? > ')
while True:
    driver = webdriver.Chrome()
    driver.get('https://www.popsilla.com/com.innersloth.spacemafia?utm_source=bing&utm_medium=cpc&utm_campaign=PS%20-%20AU%20-%20Desktop&utm_term=among%20us&utm_content=Among%20Us')
    driver.execute_script("window.scrollTo(0, 1500)") 
    time.sleep(1)
    commentBox = driver.find_element_by_xpath('//*[@id="hypercomments_widget"]/div/div[2]/div[4]/div/div[2]/textarea')
    commentBox.click()
    commentBox.send_keys(message)

    addCommentButton = driver.find_element_by_xpath('//*[@id="hypercomments_widget"]/div/div[2]/div[4]/div/div[5]/div[2]') 
    addCommentButton.click()

    addUsername = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/input')
    addUsername.send_keys('penisman' + str(random.randint(1, 10000)))

    addEmail = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/div[2]/input')
    addEmail.send_keys(str(random.randint(1, 100000)) + "@pornhub.com")

    sendReview = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/div[3]')
    sendReview.click()
    time.sleep(1)
    driver.quit()
