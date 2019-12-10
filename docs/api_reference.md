# API Documentation
## Developer Note(s)
1. This documentation uses the [``httpie``](https://httpie.org/) application for making API calls.
2. Please note, we are using ``Djano REST Framework`` to power our API web-service.
## Register
* **URL**
  * ``127.0.0.1:8000/api/register``
* **Method**
  * ``POST``
* **Data Params**
  * first_name
  * last_name
  * email
  * username
  * password
* **URL Params**
  * None
* **Success Message**
  **Status: 201**
  ```json
  {
    "email": "varughese.juby@gmail.com",
    "first_name": "Juby",
    "last_name": "Varughese",
    "username": "juby11"
}

  ```
* **Error Message**
  **Status: 400**
  ```json
  {
    "email": [
        "This field must be unique."
    ],
    "username": [
        "This field must be unique."
    ]
}

  ```
  **Status: 400**
  ```json
  {
      "error": "The password is not secure."
  }
  ```
* **Sample Call**
  ```bash
  winpty http --form POST http://127.0.0.1:8000/api/register \
  first_name="Juby" \
  last_name="Varughese" \
  email=varughese.juby@gmail.com \
  username="juby11" \
  password=123
  ```
## Login
* **URL**
  * ``127.0.0.1:8000/api/login``
* **Method**
  * ``POST``
* **Data Params**
  * username
  * password
* **URL Params**
  * None
* **Success Message**
  **Status: 200**
  ```json
  {
    "token": "f5191a796cf1d2946a1a36306a2fba33ff0deb88"
 }
  ```
* **Error Message**
  **Status: 400**
  ```json
  {
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```
* **Sample Call**
  ```bash
winpty http --form POST http://127.0.0.1:8000/api/login username=juby11   password=123
  ```


openssl base64 -in export.xml > export.xml.base64

winpty http --form POST http://127.0.0.1:8000/api/ios-healthkit-uploads 'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a' upload_file_name=export.xml upload_file=@export.xml.base64
