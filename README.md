# WebCamDetector

A small webcam app that sends and email to the designated email when a face gets detected on camera.

## How to install

### Install the required packages

Python3 should be installed on you computer
Use pip to install the dependencies:
```console
$ python3 -m pip install -r requirements.txt
```

### Create a .env file

Create a .env file that will contain two variables: email you want it to send it to and the API Key from App Passwords from Google.

```
gmail_key = longstringofcharacters
email_user = the email you want it to send it to
```

### Get an API Key from your Google Account

This project demonstrates how to generate an app password from a Google account for secure access to Google services:

1. Go to your Google Account settings.
2. Navigate to the **Security** section.
3. Locate the **App passwords** option and click on it.
4. Select the app and device for which you want to generate an app password.
5. Follow the prompts to generate the app password.
6. Use the generated app password in your .env file in your project directory with the email.

## How to use:
Run the file:
```commandline
$ python3 main.py
```

## Other stuff to keep up:

In the emailcam.py file in line 25 you can change the two first arguments of 
```python
gmail.sendmail(email_user, email_user, email_message.as_string())
```
 The first one is the one who sends the email and the second for who it will be recieving it so you can change that and add another param in the .env file to make it more anonymous.
