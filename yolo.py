from selenium import webdriver
import time

link = str(input("Enter yolo link: "))
message = "0"
error = "errors"
print("[1] Bee Movie Script")
print("[2] Never Gonna Give You Up")
print("[3] Shrek Movie Script")
print("[4] Africa Lyrics")
print("[5] Rappin for Jesus")
script = input("Choose Spam Method: ")

driverpath="/bin/chromedriver"
driver = webdriver.Chrome(driverpath)
driver.get(link)

if script == "1":
    f = open('scripts/beemovie.txt', 'r')
    type = "Bee Movie script"
elif script == "2":
    f = open('scripts/nevergonna.txt', 'r')
    type = "Never Gonna Give You Up lyrics"
elif script == "3":
    print("No Shrek Script yet")
    type = "Shrek script"
elif script == "4":
    f = open('scripts/africa.txt', 'r')
    type = "Africa Lyrics"
elif script == "5":
    f = open('scripts/jesus.txt', 'r')
    type = "Rappin For Jesus"
#add shrek script
    
elem = driver.find_element_by_xpath('//*[@id="text"]')

TypeError = False
for line in f:
    try:
        elem = driver.find_element_by_xpath('//*[@id="text"]')
        elem.send_keys(line)
        driver.find_element_by_xpath('//*[@id="send-button"]').click()
        print("\033[1;34;40m" + "[+] Message sent: %s" % line + "\033[1;34;40m \n")
        time.sleep(2.5)
        driver.refresh()
    except BaseException or WebDriverException:
        print("\033[1;31;40m" + "[!] Message not sent: %s" % line + "\033[1;31;40m \n")
        message = "1"
        error = "error"
        break;
    
if error == "0":
    print("\033[0;37;46m" + type + " has finished with " + message + " " + error + "\033[0;37;46m \n")
else:
    print("\033[0;37;41m" + type + " has finished with " + message + " " + error + "\033[0;37;41m \n")
