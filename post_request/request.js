const axios = require('axios')
const hotpTotpGenerator = require('hotp-totp-generator')

const URL = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge';

const body = {
  github: 'https://github.com/LeoMaggio/DPS-AI-Engineer-Challenge',
  email: 'mgg.lrd@gmail.com',
  url: 'https://dps22.herokuapp.com/api/predict',
  notes:
    'Chech also my web app: https://dps22.herokuapp.com/'
};

const password = hotpTotpGenerator.totp({
  key: 'mgg.lrd@gmail.comDPSCHALLENGE',
  X: 120,
  T0: 0,
  algorithm: 'sha512',
  digits: 10
});

const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Basic ${password}`
};

axios
  .post(URL, body, {headers})
  .then((response) => console.log('Response', response))
  .catch((error) => console.log('Error', error));