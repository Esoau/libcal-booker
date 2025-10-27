import sys
from datetime import datetime, timedelta
from playwright.sync_api import Playwright, sync_playwright

FIRST_NAME = "hi"
LAST_NAME = "hi"
NETID = "qaw2944"
EMAIL_1 = "timchao2028@u.northwestern.edu"
EMAIL_2 = "timchao2027@u.northwestern.edu"
EMAIL_3 = "ycc@u.northwestern.edu"

# gets date 7 days from now
target_date = datetime.now() + timedelta(days=6)

# Format 1: "Saturday, November 1, 2025" (for the button label)
# The '%-d' removes the leading zero from the day (e.g., '1' instead of '01')
date_label_str = target_date.strftime("%A, %B %-d, %Y") 

# Format 2: "2025-11-01" (for the dropdown value)
date_value_str = target_date.strftime("%Y-%m-%d")

print(f"Targeting bookings for date: {date_label_str}")

# dynamic date for buttons
label_1_click = f"12:00am {date_label_str} - Mudd 2153 - Available"
label_1_dropdown = f"Mudd 2153: 12:00am {date_label_str},"
value_1_dropdown = f"{date_value_str} 04:00:00"

label_2_click = f"4:00am {date_label_str} - Mudd 2153 - Available"
label_2_dropdown = f"Mudd 2153: 4:00am {date_label_str},"
value_2_dropdown = f"{date_value_str} 08:00:00"

label_3_click = f"8:00am {date_label_str} - Mudd 2153 - Available"
label_3_dropdown = f"Mudd 2153: 8:00am {date_label_str},"
value_3_dropdown = f"{date_value_str} 12:00:00"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True) 
    context = browser.new_context()
    page = context.new_page()

    print("Navigating to Northwestern LibCal...")
    page.goto("https://northwestern.libcal.com/spaces?lid=925&gid=1584")

    # Click 'Next' 7 times to get to the correct week
    print("Clicking 'Next' 7 times to reach target week...")
    for i in range(7):
        page.get_by_role("button", name="Next").click()
        print(f"  Clicked 'Next' {i+1}/7")

    # booking 3
    print(f"Attempting Booking 1 (12am-4am) for {date_label_str}")
    page.get_by_label(label_1_click).click()
    page.get_by_label(label_1_dropdown).select_option(value_1_dropdown)
    page.get_by_role("button", name="Submit Times").click()
    
    print("Filling form for Booking 1...")
    page.get_by_role("textbox", name="First Name").fill(FIRST_NAME)
    page.get_by_role("textbox", name="Last Name").fill(LAST_NAME)
    page.get_by_role("textbox", name="Email *").fill(EMAIL_1)
    page.get_by_role("textbox", name="NetID *").fill(NETID)
    page.get_by_label("What is your affiliation with").select_option("Undergraduate")
    page.get_by_role("button", name="Submit my Booking").click()
    print("Booking 1 Submitted.")
    page.get_by_role("link", name="Make Another Booking").click()

    # booking 2
    print(f"Attempting Booking 2 (4am-8am) for {date_label_str}")
    page.get_by_label(label_2_click).click()
    page.get_by_label(label_2_dropdown).select_option(value_2_dropdown)
    page.get_by_role("button", name="Submit Times").click()

    print("Filling form for Booking 2...")
    page.get_by_role("textbox", name="First Name").fill(FIRST_NAME)
    page.get_by_role("textbox", name="Last Name").fill(LAST_NAME)
    page.get_by_role("textbox", name="Email *").fill(EMAIL_2)
    page.get_by_role("textbox", name="NetID *").fill(NETID)
    page.get_by_label("What is your affiliation with").select_option("Undergraduate")
    page.get_by_role("button", name="Submit my Booking").click()
    print("Booking 2 Submitted.")
    page.get_by_role("link", name="Make Another Booking").click()

    # booking 3
    print(f"Attempting Booking 3 (8am-12pm) for {date_label_str}")
    page.get_by_label(label_3_click).click() 
    page.get_by_label(label_3_dropdown).select_option(value_3_dropdown)
    page.get_by_role("button", name="Submit Times").click()

    print("Filling form for Booking 3...")
    page.get_by_role("textbox", name="First Name").fill(FIRST_NAME)
    page.get_by_role("textbox", name="Last Name").fill(LAST_NAME)
    page.get_by_role("textbox", name="Email *").fill(EMAIL_3)
    page.get_by_role("textbox", name="NetID *").fill(NETID)
    page.get_by_label("What is your affiliation with").select_option("Undergraduate")
    page.get_by_role("button", name="Submit my Booking").click()
    print("Booking 3 Submitted.")

    print("All bookings complete. Closing browser.")
    context.close()
    browser.close()


# --- This is the part that starts the script ---
with sync_playwright() as playwright:
    run(playwright)
