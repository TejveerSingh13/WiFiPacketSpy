from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
import time

def CaptureGoogle():
    #Define the website and output file name
    website_url = "https://www.google.com"
    output_file = "./all_packets.pcap"
    search_query = "what is the square root of 99"

    # Start the Chrome web browser
    driver = webdriver.Chrome()

    # Define the command to start tshark
    tshark_command = ["tshark", "-i", "Wi-Fi", "-w", output_file]
    capture_process = subprocess.Popen(tshark_command)

    # Try to capture network traffic
    try:
        # Navigate to the website
        driver.get(website_url)
        time.sleep(1)
        
        # Add your Selenium interactions here, such as performing searches or navigating the site.
        search_input = driver.find_element(by="name", value="q")
        search_input.send_keys(search_query)
        time.sleep(0.2)
        search_input.send_keys(Keys.RETURN)
        
        # Wait for some time to capture network traffic
        time.sleep(1)  # Adjust the time as needed

    finally:
        # Close the web browser
        driver.quit()

        # Stop the packet capture process
        capture_process.terminate()
        capture_process.wait() 

def CaptureYoutube():
    #Define the website and output file name
    website_url = "https://www.youtube.com"
    output_file = "./youtube.pcap"
    search_query = "Shape of You Ed Sheeran"

    # Start the Chrome web browser
    driver = webdriver.Chrome()

    # Define the command to start tshark
    tshark_command = ["tshark", "-i", "Wi-Fi", "-w", output_file]
    capture_process = subprocess.Popen(tshark_command)

    # Try to capture network traffic
    try:
        # Navigate to the website
        driver.get(website_url)
        time.sleep(1)
        
        # Add your Selenium interactions here, such as performing searches or navigating the site.
        search_input = driver.find_element(by="name", value="search_query")
        search_input.send_keys(search_query)
        time.sleep(0.2)
        search_input.submit()
        
        # Wait for some time to capture network traffic
        time.sleep(1)  # Adjust the time as needed

    finally:
        # Close the web browser
        driver.quit()

        # Stop the packet capture process
        capture_process.terminate()
        capture_process.wait()

def CaptureWiki():
    #Define the website and output file name
    website_url = "https://www.wikipedia.org/"
    output_file = "./wiki.pcap"
    search_query = "University of Colorado, Denver"

    # Start the Chrome web browser
    driver = webdriver.Chrome()

    # Define the command to start tshark
    tshark_command = ["tshark", "-i", "Wi-Fi", "-w", output_file]
    capture_process = subprocess.Popen(tshark_command)

    # Try to capture network traffic
    try:
        # Navigate to the website
        driver.get(website_url)
        time.sleep(1)
        
        # Add your Selenium interactions here, such as performing searches or navigating the site.
        search_input = driver.find_element(by="name", value="search")
        search_input.send_keys(search_query)
        time.sleep(0.2)
        search_input.submit()
        
        # Wait for some time to capture network traffic
        time.sleep(1)  # Adjust the time as needed

    finally:
        # Close the web browser
        driver.quit()

        # Stop the packet capture process
        capture_process.terminate()
        capture_process.wait()

def CaptureAmazon():
    #Define the website and output file name
    website_url = "https://www.amazon.com/"
    output_file = "./amazon.pcap"
    search_query = "leg"

    # Start the Chrome web browser
    driver = webdriver.Chrome()

    # Define the command to start tshark
    tshark_command = ["tshark", "-i", "Wi-Fi", "-w", output_file]
    capture_process = subprocess.Popen(tshark_command)

    # Try to capture network traffic
    try:
        # Navigate to the website
        driver.get(website_url)
        time.sleep(1)
        
        # Add your Selenium interactions here, such as performing searches or navigating the site.
        search_input = driver.find_element(by="name", value="field-keywords")
        search_input.send_keys(search_query)
        time.sleep(0.2)
        search_input.submit()
        
        # Wait for some time to capture network traffic
        time.sleep(1)  # Adjust the time as needed

    finally:
        # Close the web browser
        driver.quit()

        # Stop the packet capture process
        capture_process.terminate()
        capture_process.wait()

def CaptureYahoo():
    #Define the website and output file name
    website_url = "https://www.yahoo.com/"
    output_file = "./yahoo.pcap"
    search_query = "how to pass college"

    # Start the Chrome web browser
    driver = webdriver.Chrome()

    # Define the command to start tshark
    tshark_command = ["tshark", "-i", "Wi-Fi", "-w", output_file]
    capture_process = subprocess.Popen(tshark_command)

    # Try to capture network traffic
    try:
        # Navigate to the website
        driver.get(website_url)
        time.sleep(1)
        
        # Add your Selenium interactions here, such as performing searches or navigating the site.
        search_input = driver.find_element(by="name", value="p")
        search_input.send_keys(search_query)
        time.sleep(0.2)
        search_input.submit()
        
        # Wait for some time to capture network traffic
        time.sleep(1)  # Adjust the time as needed

    finally:
        # Close the web browser
        driver.quit()

        # Stop the packet capture process
        capture_process.terminate()
        capture_process.wait()

CaptureAmazon()
print("Capturing done!")
