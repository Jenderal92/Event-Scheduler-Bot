# Event Scheduler Bot

![event-scheduler-bot Jenderal92](https://github.com/user-attachments/assets/196a5e7f-fcbc-4569-9bed-525a070fee42)


**Event Scheduler Bot** is a Python-based tool that automates Google Calendar tasks. With this bot, you can create, list, and delete events directly from your terminal. It uses the Google Calendar API to interact with your calendar.

---

## Features

1. **Create New Events**:
   - Add event details such as title, location, description, date, and time.
   - Automatically generate an Event ID and shareable event link.

2. **List Upcoming Events**:
   - View a list of the next 10 events from your Google Calendar.
   - Display event start time and title.

3. **Delete Events**:
   - Delete events using their Event ID.

4. **User Input Validation**:
   - Ensures all inputs (date, time, etc.) follow the correct format.

---

## Prerequisites

1. **Python 2.7**: This tool is compatible with Python 2.7.
2. **Google API Client Library**:
   - Install it using `pip install --upgrade google-api-python-client oauth2client`.
3. **Google Calendar API**:
   - Enable the Google Calendar API for your Google Cloud project.
4. **Credential Files**:
   - Download the `credentials.json` file from the Google Cloud Console and place it in the same directory as the script.

## How to Obtain `credentials.json`

The `credentials.json` file is required to authenticate your application with the Google Calendar API. Follow these steps to get it:

---

#### **1. Go to Google Cloud Console**
- Open the [Google Cloud Console](https://console.cloud.google.com/).
- Log in with your Google account.

---

#### **2. Create or Select a Project**
- If you don’t have a project:
  1. Click **"Create Project"**.
  2. Enter a project name (e.g., "Event Scheduler Bot").
  3. Click **"Create"**.
- If you already have a project:
  - Select the project you want to use.

---

#### **3. Enable Google Calendar API**
1. In the navigation menu, go to **"API & Services"** > **"Library"**.
2. Search for **"Google Calendar API"** in the search box.
3. Click on **"Google Calendar API"**, then click the **"Enable"** button.

---

#### **4. Create Credentials**
1. Go to **"API & Services"** > **"Credentials"**.
2. Click the **"Create Credentials"** button and select **"OAuth client ID"**.
3. If prompted to configure the OAuth consent screen:
   - Click **"Configure consent screen"**.
   - Choose **"External"**.
   - Fill in details like the app name (e.g., "Event Scheduler Bot").
   - Click **"Save and Continue"** until the process is complete.
4. Select **"Desktop app"** as the application type.
5. Click **"Create"**.
6. Download the `credentials.json` file and save it in the same directory as your Python script.

---

#### **5. Ensure `credentials.json` is in the Correct Location**
- Place the `credentials.json` file in the directory where you are running the Python script.
- Ensure the file is named **credentials.json** for the script to recognize it.

---

#### **6. Run the Script to Generate a Token**
- Execute the Python script:
  ```bash
  python event_scheduler_bot.py
  ```
- On the first run, you’ll be prompted to log in to your Google account.
- The script will automatically save the authentication token in a file called `token.json`.

---

#### **Important Notes**
- **Do not share your `credentials.json` or `token.json` files** with anyone, as they contain sensitive information that grants access to your Google Calendar.
- If you encounter issues, ensure:
  - The Google Calendar API is enabled for your project.
  - You’re using the same Google account when logging in during the script’s execution.

---

## Setup Instructions

1. Clone the repository or download the script file.
2. Ensure `credentials.json` is in the same directory.
3. Install dependencies:
   ```bash
   pip install --upgrade google-api-python-client oauth2client
   ```
4. Run the script:
   ```bash
   python event_scheduler_bot.py
   ```

---

## Usage

### Menu Options

- **1. Create a New Event**:
  - Enter event details as prompted.
  - Example input:
    ```
    Event Title: Meeting
    Location: Office
    Description: Team meeting
    Date: 2025-01-01
    Start Time: 10:00
    End Time: 11:00
    ```
  - Output:
    ```
    Event created successfully!
    Event ID: abc123xyz456
    Event Link: https://www.google.com/calendar/event?eid=abc123xyz456
    ```

- **2. List Upcoming Events**:
  - Lists the next 10 events, displaying the date and title.

- **3. Delete an Event**:
  - Enter the Event ID from the list or creation output to delete an event.

- **4. Exit**:
  - Exit the program.

---

## Example

### Creating a New Event

```plaintext
--- Create a New Event ---
Event Title: Team Meeting
Location: Office
Description: Monthly team discussion
Date: 2025-01-10
Start Time: 10:00
End Time: 11:30
Event created successfully!
Event ID: abc123xyz456
Event Link: https://www.google.com/calendar/event?eid=abc123xyz456
```

### Listing Events

```plaintext
--- Upcoming Events ---
2024-12-25T22:30:00+07:00 - Christmas Party
2025-01-10T10:00:00+07:00 - Team Meeting
```

### Deleting an Event

```plaintext
--- Delete an Event ---
Enter Event ID to delete: abc123xyz456
Event deleted successfully.
```

---

## Limitations

- Requires an active internet connection to interact with Google Calendar API.
- Only supports basic event creation, listing, and deletion.

---
