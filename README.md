# Entity_Validator_API

* This project includes a Django App which has 2 REST APIs.
* POST API for validation of an entity if it belongs in a finite set.
* POST API for validation of an entity based on numeric constraints.
* Django App is runnable via Docker.

---

### POST API to validate a slot with a finite set of values -
- Validate an entity on the basis of its value extracted.
- The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

Sample Request:


```
{
  "invalid_trigger": "invalid_ids_stated",
  "key": "ids_stated",
  "name": "govt_id",
  "reuse": true,
  "support_multiple": true,
  "pick_first": false,
  "supported_values": [
    "pan",
    "aadhaar",
    "college",
    "corporate",
    "dl",
    "voter",
    "passport",
    "local"
  ],
  "type": [
    "id"
  ],
  "validation_parser": "finite_values_entity",
  "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
  ]
}
```
The input should be in this format exactly. The data referenced in the keys of the JSON can differ though.
* _pick_first (bool)_ : Set to true if the first value is to be picked up.
* _support_multiple (bool)_ : Set to true if multiple entities are supported.
* _values (List[Dict])_ : Entity values to be checked are sent in values.
* _supported_values (List[str])_ : List of supported values for the entity value.
* _invalid_trigger (str)_ : Trigger to use if the extracted value is not supported.
* _key (str)_ : Dict key to use in the parameters returned.

Sample Response based on sample request:
```
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "ids_stated": ["COLLEGE"]
    }
}
```
Response Format:
```
{
    "filled": <filled flag>,
    "partially_filled": <partially filled flag>,
    "trigger": <trigger value>,
    "parameters": <Dict with request key as key and list of validated entities as value>
}
```
* _filled_ : **True** if all values are valid
* _partially_filled_ : **True** in following cases - 
    * when a subset of values are valid.
    * when there are values and none of them are valid.


* _pick_first_ : If **True** in request, the **ids_stated** in params must be a string instead of a list.
* _support_multiple_ : If **true** in the sample request, the **ids_stated** must be a list of supported IDs passed in the values list.

---

### POST API to validate a slot with a numeric value extracted and constraints on the value extracted -
- Validate an entity on the basis of its value extracted.
- The API will check if that value satisfies the numeric constraints put on it.
- If there are no numeric constraints, it will simply assume the value is valid.
﻿
- If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
- In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.
- If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be partially filled.
﻿

Sample Request:
```
{
  "invalid_trigger": "invalid_age",
  "key": "age_stated",
  "name": "age",
  "reuse": true,
  "pick_first": true,
  "type": [
    "number"
  ],
  "validation_parser": "numeric_values_entity",
  "constraint": "x>=18 and x<=30",
  "var_name": "x",
  "values": [
    {
      "entity_type": "number",
      "value": 23
    }
  ]
}
```
The input should be in this format exactly. The data referenced in the keys of the JSON can differ though.
* _pick_first (bool)_ : Set to true if the first value is to be picked up.
* _support_multiple (bool)_ : Set to true if multiple entities are supported.
* _values (List[Dict])_ : Entity values to be checked are sent in values.
* _invalid_trigger (str)_ : Trigger to use if the extracted value is not supported.
* _key (str)_ : Dict key to use in the parameters returned.
* _constraint (str)_ : Constraint which numeric value should follow in order to validate. The constraint expression will follow python syntax.
* _var_name (str)_ : Var used inside the constraint in place of numeric value.

Sample Response based on sample request:
```
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "age_stated": 23
    }
}
```
Response Format:
```
{
    "filled": <filled flag>,
    "partially_filled": <partially filled flag>,
    "trigger": <trigger value>,
    "parameters": <Dict with request key as key and list of validated entities as value>
}
```
* _filled_ : **True** if all values are valid
* _partially_filled_ : **True** in following cases - 
    * when a subset of values are valid.
    * when there are values and none of them are valid.


* _pick_first_ : If **True** in request, the **ids_stated** in params must be a string instead of a list.
* _support_multiple_ : If **true** in the sample request, the **ids_stated** must be a list of supported IDs passed in the values list.

---


## Requirements - 
The following are the requirements for the project, which will be installed in the docker automatically while creating docker file -

* django
* djangorestframework
* danjo-rest-swagger
* marshmallow

Note - Marshmallow is used in this project to validate the incoming data and then convert it into python class object.
Here, the validation means is to check if the required fields are given or not in the request.

---

## Docker - 
Dockerfile is created inside the repository which contains the steps to create a docker image.

Size of Docker image will be approx 970 MB.

To build the docker image from docker file - 
 * Download project and go to project directory.
 * Run following command in terminal or powershell - 
    * docker build --tag <image_name>:<image_version> .
    * Eg - docker build --tag entity_validator:v1 .
  
Docker image can also be directly pulled using the following command - 
 * docker pull kanshul03/entity_validator:v1
  
Once the docker image is built, run the following command to run the image -
* docker run -p 8080:8080 -t <image_name>:<image_version>
* Eg - docker run -p 8080:8080 -t entity_validator:v1

OR
 * docker run -p 8080:8080 -t kanshul03/entity_validator:v1
---

## Running Django App - 
* To use Post api service for finite value entity, open -
    *  [http://localhost:8080/validate/finite_values/](http://localhost:8080/validate/finite_values/)
    
* To use Post api service for numeric entity, open -
    * [http://localhost:8080/validate/numeric_constraints/](http://localhost:8080/validate/numeric_constraints/)
    
* To see Swagger-docs, open -
    * [http://localhost:8080/swagger-docs/](http://localhost:8080/swagger-docs/)
 
 
