from selenium import webdriver
import time

try:
    chrome_driver = "/opt/packages/chromedriver"  #chromedriver路径
    browser = webdriver.Chrome(executable_path=chrome_driver)

    browser.get('https://shimo.im/welcome')    #请求石墨文档官网链接
    time.sleep(1)

    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm1.click()
    time.sleep(1)

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('phone')  #请将phone替换为您的石墨账号
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('password')    #请将password替换为您的密码
    time.sleep(1)
    browser.find_element_by_xpath('//*[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()

    cookies = browser.get_cookies()  # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()