# BioDB Software Requirement Specification (SRS)

## A webapp used to get Apple HealthKit data and provide a dashboard for it

# Use Cases:
## (1). Login / Logout
### Use “token based authentication” for security purposes
* **URL**

  * ``127.0.0.1:8000/api/login``
  * ``127.0.0.1:8000/api/logout``


* **Method**

  * ``POST``


* **Data Params**

  * username
  * password


* **URL Params**

  * None


## (2). Register
* **URL**

  * ``127.0.0.1:8000/api/register``


* **Method**

    * ``POST``


* **Data Params**

  * First name
  * Last name
  * Email
  * Username
  * Password


## (3) Dashboard
#### A summary page displaying graphs of the health data.
* **Url**

  * ``127.0.0.1:8000/api/dashboard``


* **Method**

    * ``POST``

* **Fields**
    * username
    * sensors list
    * Name (Apple calls it “Attribute”)    Steps Count
    * X-Axis: Creation Date - (Unit of measure: Date)
    * Y-Axis: Steps Count - (Unit of measure: Count)


* **Data List**

    * value
    * creation_date

## (4) Upload HealthKit File
#### User uploads their exported XML data file to our webapp

* **Url**

  * ``127.0.0.1:8000/api/api/ios-healthkit-uploads``


* **Method**

    * ``POST``


* **Field**

    * upload_file
    * upload_file_name

## (5) List all uploaded files
#### The user will be able to get all the uploads that they did and not other people, so the system has to filter properly

* **Url**

  * ``127.0.0.1:8000/api/list/ios-healthkit-uploads``


* **Method**

    * ``GET``


## (6) Instrument Details Page
#### The user is able to get more detailed statistics on the instrument they want to view

* **Url**

  * ``127.0.0.1:8000/api/sensor/<sensor_id>``


* **Method**

    * ``GET``


* **Fields**
    * Mean
    * Median
    * Mode


* **Data List**
    * Value
    * Time


## (5) Profile API
* **Url**

  * ``127.0.0.1:8000/api/user_profile``
* **Method**

    * ``POST``

* **Fields**
    * email
    * first_name
    * last_name
    * username
