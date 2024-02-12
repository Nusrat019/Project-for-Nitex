import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class EventSchedulerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_create_event(self):
        # Navigate to the Event Scheduler page
        self.driver.get("https://yourwebsite.com/event_scheduler")
        self.assertIn("Event Scheduler", self.driver.title)

        # Fill in the event creation form
        event_name = "Test Event"
        event_date = "2024-02-12"
        participant_emails = "participant1@example.com,participant2@example.com"

        event_name_input = self.driver.find_element_by_id("event_name")
        event_name_input.send_keys(event_name)

        event_date_input = self.driver.find_element_by_id("event_date")
        event_date_input.send_keys(event_date)

        participant_emails_input = self.driver.find_element_by_id("participant_emails")
        participant_emails_input.send_keys(participant_emails)

        # Submit the form to create a new event
        submit_button = self.driver.find_element_by_id("submit_button")
        submit_button.click()

        # Wait for the event to be created and appear in the list
        time.sleep(2)  # Adjust as needed depending on the application's response time

        # Verify that the event appears in the user's event list with the correct details
        event_list = self.driver.find_element_by_id("event_list")
        events = event_list.find_elements_by_class_name("event")

        event_found = False
        for event in events:
            if event.find_element_by_class_name("event_name").text == event_name and \
               event.find_element_by_class_name("event_date").text == event_date and \
               event.find_element_by_class_name("participant_emails").text == participant_emails:
                event_found = True
                break

        self.assertTrue(event_found, "Event not found in the event list")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
