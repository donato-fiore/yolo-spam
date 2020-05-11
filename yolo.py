from selenium import webdriver
import time

links = input("Enter yolo link: ")
link = str(links)

print("[1] Bee Movie Script")
print("[2] Never Gonna Give You Up")
print("[3] Shrek Movie Script")
print("[4] Africa Lyrics")
script = input("Choose Spam Method: ")

driverpath="/bin/chromedriver"
driver = webdriver.Chrome(driverpath)
driver.get(link)
filler = ("filler")


if script == "1":
    f = open('/home/pi/Desktop/scripts/beemovie.txt', 'r')
elif script == "2":
    f = open('/home/pi/Desktop/scripts/nevergonna.txt', 'r')
elif script == "3":
    print("No Shrek Script yet")
elif script == "4":
    f = open('/home/pi/Desktop/scripts/africa.txt', 'r')
#add shrek script
    
elem = driver.find_element_by_xpath('//*[@id="text"]')

TypeError = False
for line in f:
    try:
        elem = driver.find_element_by_xpath('//*[@id="text"]')
        elem.send_keys(line)
        driver.find_element_by_xpath('//*[@id="send-button"]').click()
        time.sleep(2.5)
        driver.refresh()
        print("[+] Message sent: %s" % line)
    except TypeError:
        print("[!] Message not sent: %s" % line)
        break;      