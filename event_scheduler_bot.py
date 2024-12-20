#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import httplib2
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from apiclient.discovery import build
import re

def print_banner():
    banner = """
          Welcome to Event Scheduler Bot !
          Automate your Google Calendar!
    """
    print(banner)

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

def authenticate_google():
    """Authenticate Google Calendar API."""
    store = Storage(TOKEN_FILE)
    creds = store.get()
    if not creds or creds.invalid:
        flow = flow_from_clientsecrets(CREDENTIALS_FILE, SCOPES)
        creds = run_flow(flow, store)
    return creds

def validate_input(prompt, pattern=None, empty_allowed=False):
    """Function to validate input from the user."""
    while True:
        user_input = raw_input(prompt)
        if not empty_allowed and not user_input.strip():
            print("Input cannot be empty. Please try again.")
        elif pattern and not re.match(pattern, user_input):
            print("Invalid format. Please follow the correct format.")
        else:
            return user_input

def create_event(service):
    """Create a new calendar event."""
    print("\n--- Create a New Event ---")
    
    summary = validate_input("Event Title: ", empty_allowed=False)
    location = validate_input("Location (optional): ", empty_allowed=True)
    description = validate_input("Description (optional): ", empty_allowed=True)
    
    date = validate_input("Date (YYYY-MM-DD): ", pattern=r"\d{4}-\d{2}-\d{2}", empty_allowed=False)
    start_time = validate_input("Start Time (HH:MM): ", pattern=r"\d{2}:\d{2}", empty_allowed=False)
    end_time = validate_input("End Time (HH:MM): ", pattern=r"\d{2}:\d{2}", empty_allowed=False)
    
    start_datetime = "{}T{}:00".format(date, start_time)
    end_datetime = "{}T{}:00".format(date, end_time)

    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'Asia/Jakarta',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Asia/Jakarta',
        },
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()

    print("Event created successfully!")
    print("Event ID: {}".format(created_event.get('id')))
    print("Event Link: {}".format(created_event.get('htmlLink')))

def list_events(service):
    """List upcoming calendar events."""
    print("\n--- Upcoming Events ---")
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print("No upcoming events found.")
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print("{} - {}".format(start, event['summary']))

def delete_event(service):
    """Delete a calendar event."""
    print("\n--- Delete an Event ---")
    event_id = validate_input("Enter Event ID to delete: ", empty_allowed=False)
    service.events().delete(calendarId='primary', eventId=event_id).execute()
    print("Event deleted successfully.")

def main():
    print_banner()
    creds = authenticate_google()
    service = build('calendar', 'v3', http=creds.authorize(httplib2.Http()))

    while True:
        print("\nMenu:")
        print("1. Create a new event")
        print("2. List upcoming events")
        print("3. Delete an event")
        print("4. Exit")
        choice = validate_input("Choose an option (1-4): ", pattern=r"[1-4]", empty_allowed=False)

        if choice == '1':
            create_event(service)
        elif choice == '2':
            list_events(service)
        elif choice == '3':
            delete_event(service)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
