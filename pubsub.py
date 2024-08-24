# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
	This is my personal script that I use to pre-order a sub sandwich for pickup from my local Publix grocery.
	It is completely tailored to my personal preferences of sandwich. This sandwich by default will be:

	- A chicken tender sub
	- On Italian 5 Grain bread
	- With Muenster cheese
	- Without tomatoes
	- With salt and pepper
	- Including oil and vinegar packets
	- With olives and pickles
	- With BBQ sauce
	- Toasted

	The procedure of this automation script is as follows:

	1. Go to the Publix website
	2. Search for a "publix chicken tender sub" and click on it to begin customizing it
	3. Customize sandwich and add it to cart
	4. Confirm store location
	5. Enter contact information and schedule time for sandwich to be made for pickup
	6. End right before submitting final confirmation for user to manually review and place

	IMPORTANT: "PATH" variable must be changed to the location of the chromedriver on your machine!
	You must have chromedriver installed for this script to work.

	Additionally, the "first_name", "last_name", "phone_number", and "email_address" must be changed.
"""

# Copyright (c) 2024 Aaron Galentine
# All rights reserved.

# This is free software; you can redistribute it and/or modify it under the terms of the AGPL-3.0 License.
# This software is distributed "as is", without any guarantees of any kind, express or implied.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Gives us access to enter key, escape key, etc
from selenium.webdriver.common.by import By # For explicit wait
from selenium.webdriver.support.wait import WebDriverWait # For explicit wait
from selenium.webdriver.support import expected_conditions as EC # For explicit wait

import time # For sleep statements

# Configures appropriate chromedriver
PATH = 'C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe' # <--- CHANGE THIS VARIABLE
driver = webdriver.Chrome(PATH) # Makes it so that Chrome will open the next website as the set driver

driver.maximize_window() # Maximizes window
driver.implicitly_wait(20) # Gives an implicit wait for 20 seconds, allowing webpage to load


try:
	driver.get("https://www.publix.com/") # Opens Publix's website

	search = driver.find_element(By.ID, "searchInputFlyout") # Identifies the search bar
	search.send_keys("publix chicken tender sub") # Searches for a string in the search box
	search.send_keys(Keys.RETURN) # Sends an Enter key so that we search

	# Explicit wait for the first result of the search to be present
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]"))
		)
	first_search_result = driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]")
	first_search_result.click() # Click on first search result

	# Handles scenario where feedback window will randomly appear
	#if (EC.presence_of_element_located((By.ID, "fsrInvite"))) : 
		#close_invite_button = driver.find_element(By.CLASS_NAME, "fsrAbandonButton")
		#close_invite_button.click()

	# Waits for sub sandwich to be customizable, and then begins customizing it
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[2]/div[2]/div[2]/label"))
	)
	bread = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[2]/div[2]/div[2]/label")
	bread.click()
	print("Bread chosen.")

	# Page Down to load the other elements and continue customizing sub sandwich
	bread.send_keys(Keys.PAGE_DOWN)

	cheese = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[3]/div[2]/div[6]/label")
	cheese.click()
	print("Cheese chosen.")

	cheese.send_keys(Keys.PAGE_DOWN)

	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[2]/label"))
	)

	no_tomatoes = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[2]/label")
	no_tomatoes.click()
	print("Tomatoes removed.")

	black_pepper = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[4]/label")
	black_pepper.click()
	print("Pepper added.")

	salt = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[5]/label")
	salt.click()
	print("Salt added.")

	oil_packets = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[7]/label")
	oil_packets.click()
	print("Oil packets included.")

	vinegar_packets = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[8]/label")
	vinegar_packets.click()
	print("Vinegar packets included.")

	black_olives = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[9]/label")
	black_olives.click()
	print("Olives added.")

	black_olives.send_keys(Keys.PAGE_DOWN)

	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[13]/label"))
	)

	dill_pickles = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[13]/label")
	dill_pickles.click()
	print("Pickles added.")

	dill_pickles.send_keys(Keys.PAGE_DOWN)
	time.sleep(1) # Unfortunately required because explicit wait does not solve the issue

	#element = WebDriverWait(driver, 10).until(
		#EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[11]/div/fieldset/div[2]/div/button"))
	#)

	bbq_sauce = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[11]/div/fieldset/div[2]/div/button")
	bbq_sauce.click()
	print("BBQ sauce added.")

	bbq_sauce.send_keys(Keys.PAGE_DOWN)

	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[7]/div[2]/div[2]/label"))
	)

	toast_it = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div/div[1]/div[2]/fieldset[7]/div[2]/div[2]/label")
	toast_it.click()
	print("Sub toasted.")

	# Add the sub to the order once we are done customizing it
	add_to_order = driver.find_element(By.XPATH, "//*[@id='builder-add-to-order-btn-sticky']/span")
	add_to_order.click()
	print("Added sub to order.")

	# Go to the final pages where we confirm the store location and check out
	review_order = driver.find_element(By.XPATH, "//*[@id='navBar']/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/button/span")
	review_order.click()
	print("Reviewing order.")

	confirm_store = driver.find_element(By.ID, "confirmation-btn")
	confirm_store.click()
	print("Confirmed store.")

	checkout = driver.find_element(By.XPATH, "//*[@id='two-column-container']/div[2]/div/div/div/div[3]/button/span")
	checkout.click()
	print("Checking out.")

	# Each field we type in here has an ID that has a non-static integer at the end so we have to account for this
    # For the first name, we specifically find IDs that start with "input_FirstName" with any characters afterwards
    # "f" is required for "starts-with" to format it in a way that is a valid XPath expression
	first_name = driver.find_element(By.XPATH, f"//*[starts-with(@id, '{'input_FirstName'}')]") # Integer on the end of the ID is not static
	first_name.click()
	first_name.send_keys("John") # <--- CHANGE THIS VARIABLE
	print("First name entered.")

	# Same strategy here for the last name, phone number, and email
	last_name = driver.find_element(By.XPATH, f"//*[starts-with(@id, '{'input_LastName'}')]") # Integer on the end of the ID is not static
	last_name.click()
	last_name.send_keys("Doe") # <--- CHANGE THIS VARIABLE
	print("Last name entered.")

	phone_number = driver.find_element(By.XPATH, f"//*[starts-with(@id, '{'input_ContactPhone'}')]") # Integer on the end of the ID is not static
	phone_number.click()
	phone_number.send_keys("5555555555") # <--- CHANGE THIS VARIABLE
	print("Phone number entered.")

	phone_number.send_keys(Keys.PAGE_DOWN)

	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, f"//*[starts-with(@id, '{'input_Email'}')]")) # Integer on the end of the ID is not static
	)

	email_address = driver.find_element(By.XPATH, f"//*[starts-with(@id, '{'input_Email'}')]") # Integer on the end of the ID is not static
	email_address.click()
	email_address.send_keys("johndoe@aol.com") # <--- CHANGE THIS VARIABLE
	print("Email address entered.")

	# Once our contact information is entered, we go to the next section to choose when we want the sandwich made
	next_button_1 = driver.find_element(By.XPATH, "//*[@id='content_26']/form/div[3]/button/span[2]")
	next_button_1.click()
	print("All contact information submitted.")

	# Automatically set the sandwich to be made ASAP
	next_button_2 = driver.find_element(By.XPATH, "//*[@id='content_33']/form/div[3]/div/button/span[2]")
	next_button_2.click()
	print("Pickup time scheduled for 'ASAP'.")

	# Leave the final confirmation for the user to handle at the very end!
	print("Your sub is ready to order. Please manually review and confirm your order.")

# Exception error handling with more information on fail - will provide problem element
except Exception as e:
    print(f"Element not found: {e}")