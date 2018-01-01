from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name=input('Enter Name: ')
msg=input('Enter the message: ')
count = int(input('Enter the count: '))

input('Enter Anything to COntinue')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('input-container')
for i in range(count):
	msg_box.send_keys(msg)
	driver.find_element_by_class_name('compose-btn-send').click()