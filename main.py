from selenium import webdriver

print("Masukkan NPM Anda : ")
npm = input()

print("Masukkan Password SIAP Anda : ")
password= input()

driver = webdriver.Chrome()

driver.get("http://siap.poltekpos.ac.id/siap/besan.depan.php")

driver.find_element_by_name("user_name").send_keys(npm)
driver.find_element_by_name("user_pass").send_keys(password)
driver.find_element_by_name("login").click()