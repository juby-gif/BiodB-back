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
  # FOR USER LOGIN
  winpty http --form POST http://127.0.0.1:8000/api/login \
  username=juby11 \
  password=123

  ```
## Apple HealthKit Upload
* **URL**

  * ``127.0.0.1:8000/api/ios-healthkit-uploads``


* **Method**

  * ``POST``


* **Data Params**

  * upload_file_name
  * upload_file


* **URL Params**

  * None


* **Success Message**
  **Status: 200**
  ```json
      data={
            'detail': serializer.data,
            'Updation Status': "Succesfully Uploaded",
        }
  ```
* **Error Message**
  **Status: 400**
  ```json
  data={
            'detail': {}
            'Updation Status': "File Upload Failed",
        }
```
* **Sample Call**
  ```bash
  winpty http --form POST http://127.0.0.1:8000/api/ios-healthkit-uploads \
  'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a' \
  upload_file=export.xml \
  upload_file_name="@export.xml.base64"
  ```
## Apple HealthKit List Data
* **URL**

  * ``127.0.0.1:8000/api/list``


* **Method**

  * ``GET``


* **Data Params**

  * None


* **URL Params**

  * None


* **Success Message**
  **Status: 200**
  ```json
      data={
    "count": 13329,
    "next": "http://127.0.0.1:8000/api/list?page=2",
    "previous": null,
    "results": [
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-05-05",
            "value": 52.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-18",
            "value": 620.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-18",
            "value": 43.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-16",
            "value": 557.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-18",
            "value": 918.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-18",
            "value": 381.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-18",
            "value": 1315.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-18",
            "value": 10.0
        },
        {
            "attribute_name": "HKQuantityTypeIdentifierStepCount",
            "creation_date": "2019-03-18",
            "value": 605.0
        },
        {
           "attribute_name": "HKQuantityTypeIdentifierStepCount",
           "creation_date": "2019-03-18",
           "value": 23.0
       }
       ]
     }
  ```
* **Error Message**
  **Status: 400**
  ```json
  data={
            'data': {},
        }
```
* **Sample Call**
  ```bash
  winpty http --form http://127.0.0.1:8000/api/list \
  'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

  ```
## Apple HealthKit Upload List
* **URL**

  * ``127.0.0.1:8000/api/list/ios-healthkit-uploads``


* **Method**

  * ``GET``


* **Data Params**

  * None


* **URL Params**

  * None


* **Success Message**
  **Status: 200**
  ```json
    {
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
      {
          "data_file": "http://127.0.0.1:8000/api/list/uploads/2019/12/10/export.xml"
      },
      {
          "data_file": "http://127.0.0.1:8000/api/list/uploads/2019/12/17/export.xml"
      }
      ]
    }

  ```
* **Error Message**
  **Status: 400**
  ```json
  data={
            'data_file': {}
        }
```
* **Sample Call**
  ```bash
   winpty http --form http://127.0.0.1:8000/api/list/ios-healthkit-uploads \
   'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'
  ```
## Retrieve User Profile
* **URL**

  * ``127.0.0.1:8000/api/user-profile/retrieve``


* **Method**

  * ``GET``


* **Data Params**

  * None

* **URL Params**

  * None


* **Success Message**
  **Status: 200**
  ```json
      data={
        "email": "varughese.juby@gmail.com",
        "first_name": "Juby",
        "last_name": "Varughese",
        "username": "juby11",
      }

  ```
* **Error Message**
  **Status: 400**
  ```json
      data = {
          "detail":"Authentication credentials were not provided.",
        }
```
* **Sample Call**
  ```bash
  winpty http --form http://127.0.0.1:8000/api/user-profile/retrieve \
  'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'

  ```

## Update User Profile
* **URL**

  * ``127.0.0.1:8000/api/user-profile/update``


* **Method**

  * ``PUT``


* **Data Params**

  * email
  * first_name
  * last_name
  * username


* **URL Params**

  * None


* **Success Message**
  **Status: 200**
  ```json
      {
      "Updated data": {
          "email": "varughese.juby@gmail.com",
          "first_name": "Juby",
          "last_name": "VArughese",
          "username": "juby11"
      },
      "Updation Status": "Succesfully Updated"
      }
  ```

* **Error Message**
  **Status: 400**
  ```json
      {
    "email": [
        "This field is required."
    ],
    "first_name": [
        "This field is required."
    ],
    "last_name": [
        "This field is required."
    ],
    "username": [
        "This field is required."
    ]
    }
  ```

* **Sample Call**
  ```bash
  winpty http --form PUT http://127.0.0.1:8000/api/user-profile/update \
  'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a' \
  email=varughese.juby@gmail.com \
  first_name=Juby \
  last_name=VArughese \
  username=juby11
  ```

## Time-Series Data Filtered Statistics Calculator
* **URL**

  * ``127.0.0.1:8000/api/tsd``


* **Method**

  * ``GET``


* **Data Params**

  * None


* **URL Params**

  * attribute_name


* **Success Message**
  **Status: 200**
  ```json
  /* For Walking and Running */
        {
      "mean": 0.23,
      "median": 0.05,
      "mode": 0.0,
      "name": "HKQuantityTypeIdentifierDistanceWalkingRunning"
      }
  /* For Steps Count */
      {
    "mean": 334.88,
    "median": 96.0,
    "mode": 8.0,
    "name": "HKQuantityTypeIdentifierStepCount"
}

  ```

* **Error Message**
  **Status: 400**
  ```json
  /* For Walking and Running */
      {
      "mean": "NF",
      "median": "NF",
      "mode": "NF",
      "name": ""
      }
  /* For Steps Count */
      {
      "mean": "NF",
      "median": "NF",
      "mode": "NF",
      "name": ""
      }

  ```

* **Sample Call**
  ```bash
  winpty http http://127.0.0.1:8000/api/tsd?attribute_name='HKQuantityTypeIdentifierDistanceWalkingRunning' \
   'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'
  ```

## Time-Series Data Filter
* **URL**

  * ``127.0.0.1:8000/api/tsd-by-attribute-name``


* **Method**

  * ``GET``


* **Data Params**

  * None


* **URL Params**

  * attribute_name


* **Success Message**
  **Status: 200**
  ```json
  /* For Walking and Running */
      {
    "count": 6585,
    "next": "http://127.0.0.1:8000/api/tsd-by-attribute-name?attribute_name=HKQuantityTypeIdentifierDistanceWalkingRunning&page=2",
    "previous": null,
    "results": [
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-05-05",
          "value": 0.03803
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.45076000000000005
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.02388
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-16",
          "value": 0.42556000000000005
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.6812600000000001
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.25426
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.88873
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.0037600000000000003
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.37906999999999996
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierDistanceWalkingRunning",
          "creation_date": "2019-03-18",
          "value": 0.016380000000000002
      }
    ]
    }

  /* For Steps Count */
    {
  "count": 6744,
  "next": "http://127.0.0.1:8000/api/tsd-by-attribute-name?attribute_name=HKQuantityTypeIdentifierStepCount&page=2",
  "previous": null,
  "results": [
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-05-05",
          "value": 52.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 620.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 43.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-16",
          "value": 557.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 918.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 381.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 1315.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 10.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 605.0
      },
      {
          "attribute_name": "HKQuantityTypeIdentifierStepCount",
          "creation_date": "2019-03-18",
          "value": 23.0
      }
  ]
  }
  ```

* **Error Message**
  **Status: 200**
  ```json
  /* For Walking and Running */
      {
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
    }

  /* For Steps Count */
      {
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
    }
  ```

* **Sample Call**
  ```bash
  winpty http http://127.0.0.1:8000/api/tsd-by-attribute-name?attribute_name='HKQuantityTypeIdentifierDistanceWalkingRunning' \
   'Authorization: Token 718dbd9ec4f2783254f0266290ee5207e7281f5a'
  ```
