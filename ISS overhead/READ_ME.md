ISS Observer Application
This application is a simple Python program that sends you a notification when the International Space Station (ISS) is close enough to be visible in the night sky.

How it Works?
The application regularly checks the location of the ISS using NASA's ISS API. When the ISS is approaching close enough to be visible in the night sky, it sends you a notification via email.

Usage
If Python is not installed, download and install Python.

Download or copy this repository to your computer.

Open the Terminal or Command Prompt and navigate to the project directory.

Run the following command in the terminal or command prompt to install the required dependencies:

Copy code
pip install -r requirements.txt
Open the config.py file and edit your email information and other settings.

In the terminal or command prompt, run the following command to start the application:

css
Copy code
python main.py
The application will now check whether the ISS is in the night sky and will send you an email notification if appropriate.

Considerations
To run this application, you need a valid email account and an ISS API key.
The application uses smtplib for email sending. Depending on your email provider, you may need to update your security settings.
The application checks the ISS API at a specific frequency to determine its location. You can set this frequency in the config.py file.
Enjoy observing the ISS!

