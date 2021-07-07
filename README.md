# Covid Vaccine Slot Finder

![](https://forthebadge.com/images/badges/made-with-python.svg)

## Description
A simple python script to get the alert on vaccine slot availablity on a particular PIN code in India. Upon finding the slots in your area, A Beep Sound Would be played in a tune to get your attention so that you can book the appointments.

## Description
API's used https://apisetu.gov.in/public/api/cowin#/

## Prerequisites
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 

To install pip run in the command Line
```
python -m ensurepip -- default-pip 
``` 
to upgrade Python
```
pip install python -- upgrade
```
Shoot this command to install the Request Library:
```
pip install requests
```

## Run Script
Open Terminal or Command Prompt and type
```
python VaccSlot.py 
```
Running this script will continuously check for available slot in any Pin Code.

### Required Argument
 - PIN Code to look for vaccination slots.
 - Type of Vaccine You need Looking for

## Troubleshooting
The [www.cowin.gov.in](https://www.cowin.gov.in)'s server will block your request after some time if you continue to send request using the same IP address. 
