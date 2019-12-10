BioDB Software Requirement Specification (SRS)

A webapp used to get Apple HealthKit data and provide a dashboard for it

Use Cases:
(1) Login / Logout
Use “token based authentication” for security purposes
/api/login
Username
Password

/api/logout
(2) Register
/api/register
First name
Last name
Email
Username
Password
(3) Dashboard
A summary page displaying graphs of the health data.
URL: /api/dashboard
METHOD: GET
FIELDS:
Username
Sensors List
Name (Apple calls it “Attribute”)    Steps Count
X-Axis: Creation Date - (Unit of measure: Date)
Y-Axis: Steps Count - (Unit of measure: Count)
Data List:  
Value
Date

(4) Upload HealthKit File
User uploads their exported XML data file to our webapp
URL: /api/api/ios-healthkit-uploads
METHOD: POST
FIELDS:
upload_file
upload_file_name
(5) List all uploaded files
The user will be able to get all the uploads that they did and not other people, so the system has to filter properly
URL: /api/list/ios-healthkit-uploads
METHOD: GET
(6) Instrument Details Page
The user is able to get more detailed statistics on the instrument they want to view
URL: /api/sensor/<sensor_id>
METHOD: GET
FIELDS:
Mean
Median
Mode
Data List:
Value
Time
