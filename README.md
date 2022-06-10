# Digital Product School - AI Engineer Challenge
## Introduction
This challenge is intended for Artificial Intelligence Engineer applicants.

Their is no deadline, but keep in mind that we have limited spots for each batch. We follow the FIFO logic, the applicants who complete the mission first, will be invited first for interview.

## Mission 1: Create a AI Model
### Description
Download the “Monatszahlen Verkehrsunfälle” Dataset from the München Open Data Portal. Here you see the number of accidents for specific categories per month. Important are the first 5 columns:
```
Category
Accident-type (insgesamt means total for all subcategories)
Year
Month
Value
```
Your goal would be to visualise historically the number of accidents per category (`column1`). The dataset currently contains values until the end of 2020. Create an application that forecasts the values for:
```
Category: 'Alkoholunfälle'
Type: 'insgesamt
Year: '2021'
Month: '01'
```
## Mission 2: Publish your source code & Deploy
### Description
Publish your source code in a github repository. It should both contain the code how you made it and the visualisation itself (as an image). We’d like to see the steps how you arrived at the solution, so please make sure to commit every step you did and not just the final application in 1 or 2 commits. If you are not familiar with github, follow the instructions here.

The next step is to deploy the model. You would need to create an endpoint that returns your predictions. Make sure that your endpoint accepts a POST request with a JSON body like this:
```json
{
    "year":2020,
    "month":10
}
```
And it should return your applications prediction in the following format:
```json
{
    "prediction":value
}
```
The model can be deployed to a cloud service. You can use (aws, google cloud, heroku or whatever you prefer, they usually all provide a freetier).
## Mission 3: Send us the URL of your work
### Description
Make a POST request to the following [URL](https://dps-challenge.netlify.app/.netlify/functions/api/challenge).
### Body
The body of the request should be JSON format, like below:
```json
{
    "github":"https://github.com/ACCOUNT/REPO",
    "email":"EMAIL",
    "url":"DEPLOYED_ENDPOINT", 
    "notes":"NOTES" // Not mandatory
}
```
Fill in your email address for `EMAIL`, the path to your github repo at `ACCOUNT/REPO` and the link of your deployed model at `DEPLOYED_ENDPOINT`.

At `NOTES`, you can write some notes to us. These notes can be anything you would like us to know, especially for technical decisions. They are not mandatory, so you can also skip this this parameter.

Double-check that your email address is the same with the one you used at the application form.

### Content type
The `Content-Type` of the request must be `application/json`.

### Authorization
The URL is protected by HTTP Basic Authentication, so you have to provide an `Authorization` header. The Authorization header should be in the format:
```
Basic password
```
The password is a 10-digit time-based one-time password. To generate the password, you need to:
- Use TOTP(RFC6238). We recommend using the library [hotp-totp-generator](https://www.npmjs.com/package/hotp-totp-generator)
- Have a key. For the key use the same email address you put in the body followed by ASCII string value `DPSCHALLENGE`. For example, if your email is name@example.com, the key is
```
name@example.comDPSCHALLENGE
```
- Have some defined parameters like below:
    - TOTP's `Time Step X` is 120 seconds. `T0` is 0.
    - Use `HMAC-SHA-512` for the hash function, instead of the default `HMAC-SHA-1`.

### Sample Request
```json
POST https://dps-challenge.netlify.app/.netlify/functions/api/challenge
Authorization: Basic 0942804753 
Content-Type: application/json 

{
    "github":"https://github.com/DigitalProductschool/website",
    "email":"name@example.com",
    "url":"https://digitalproductschool.io/", 
    "notes":"I deployed using ..." // Not mandatory
}
```
### Sample Response
If your POST request succeeds, the server returns HTTP status code `200`.
```json
Status 200 OK 
{"message":"Congratulations! Achieved Mission 3"}
```
