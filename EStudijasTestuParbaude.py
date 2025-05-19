from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime

adrese1 = "https://id2.rtu.lv/openam/UI/Login"
adrese2 = "https://estudijas.rtu.lv/my/index.php?lang=en"

username='username'
password='password'

driver = webdriver.Chrome()

driver.get(adrese1)
driver.find_element("id", "IDToken1").send_keys(username)
driver.find_element("id", "IDToken2").send_keys(password)
driver.find_element("name", "Login.Submit").click()
WebDriverWait(driver, 15).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
driver.get(adrese2)
WebDriverWait(driver, 15).until(
    lambda d: d.find_element(By.CSS_SELECTOR, '[data-region="event-list-content-date"]')
)

results = []

date_sections = driver.find_elements(By.CSS_SELECTOR, '[data-region="event-list-content-date"]')
for section in date_sections:
    date_heading = section.find_element(By.CSS_SELECTOR, "h5").text.strip()

    events_list = section.find_element(By.XPATH, "following-sibling::ul[1]")

    events = events_list.find_elements(By.CSS_SELECTOR, "li.media")

    for event in events:
        try:
            task_name = event.find_element(By.TAG_NAME, 'h6').text.strip().split('\n')
            course = event.find_element(By.CSS_SELECTOR, "small.text-muted").text.strip()
            time_of_day = event.find_element(By.CSS_SELECTOR, "small.text-right").text.strip()
            results.append((course, task_name[0], f"{date_heading} {time_of_day}"))
        except:
            continue

if not results:
    print("\nNav neviena testa tuvākajā laikā")
else:
    print("\n---Testu saraksts---")
    for course, task, deadline_str in results:
        try:
            deadline = datetime.strptime(deadline_str, "%A, %d %B %Y %H:%M")
            now = datetime.now()
            delta = deadline - now
            if delta.total_seconds() > 0:
                days = delta.days
                hours, remainder = divmod(delta.seconds, 3600)
                minutes = remainder // 60
                time_remaining = f"{days}d {hours}h {minutes}m"
            else:
                time_remaining = "Nokavēts"

        except Exception as e:
            time_remaining = "Datuma kļūda"
            print(f"Error parsing date: {e}")

        print(f"Kurss: {course}")
        print(f"Uzdevums: {task}")
        print(f"Termins: {deadline_str}")
        print(f"Atlikušais laiks: {time_remaining}")
        print()


driver.quit()
