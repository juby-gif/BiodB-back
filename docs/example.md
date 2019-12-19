## We are going to test upload the file with the following code:

* **Sample Call**
  ```bash
  # FOR USER REGISTRATION
  winpty http --form POST http://127.0.0.1:8000/api/register   first_name="Juby"   last_name="Varughese"   email=varughese.juby@gmail.com   username="juby11"   password=123

  # FOR USER LOGIN
  winpty http --form POST http://127.0.0.1:8000/api/login username=juby11   password=123

  # FOR UPLOADING THE APPLE HEALTHKIT DATA FROM XML
  winpty http --form POST http://127.0.0.1:8000/api/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

  # FOR CONVERTING TO XML.BASE64
  openssl base64 -in export.xml > export.xml.base64

  # FOR EXTRACTING THE DATA FROM EXPORT.XML
  python manage.py extract_data_from_xml

  # FOR LISTING ALL THE EXTRACTED DATA FROM APPLE HEALTHKIT EXPORT DATA
  winpty http http://127.0.0.1:8000/api/list 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

  # FOR LISTING ALL THE UPLOADED FILES FOR THE USER
  winpty http http://127.0.0.1:8000/api/list/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

  # FOR FILTERING THE EXTRACTED DATA BY FILTERING AGAINST QUERY PARAMETERS WITH ATTRIBUTE-NAME = Walking and Running
  winpty http http://127.0.0.1:8000/api/tsd?attribute_name='HKQuantityTypeIdentifierDistanceWalkingRunning' 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

  # FOR FILTERING THE EXTRACTED DATA BY FILTERING AGAINST QUERY PARAMETERS WITH ATTRIBUTE-NAME - Step count
  winpty http http://127.0.0.1:8000/api/tsd?attribute_name='HKQuantityTypeIdentifierStepCount' 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

  # For running the commands using crons as background process
  python manage.py runcrons

  #For making the background process automatic
  contab -e
  */5 * * * *  source /c/Users/16474/Documents/Assignment/biodb-back/env/Scripts/activate && python /c/Users/16474/Documents/Assignment/biodb-back/biodb/manage.py runcrons > /c/Users/16474/Documents/Assignment/biodb-back/cronjob.log

  ```
