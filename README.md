# BankAPI
The project provides REST API Endpoints to list bank details given IFSC code of Bank and gives a list of banks
given Bank Name and City. The project is made in Django using DjangoRestFramework and is Deployed on Heroku.

## API EndPoints
1. Bank Detail By giving IFSC Code : http://bankapiorg.herokuapp.com/bankdetail?ifsc={ifsc_code_of_bank}
2. List of Bank with Details when given Bank Name and City :
http://bankapiorg.herokuapp.com/bankdetail?bank_name={bank_name}&city={city}
