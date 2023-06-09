# flask-calculator
Starting from the code in this repo -> https://github.com/RamonPradoMoreno/flask-tutorial
My plan is to create a more backend oriented example with a simple calculator that uses a JSON interface to communicate.

# Important Commands
* Initialize the DB:
  ```python
  flask --app flaskcalculator init-db
  ```
* Run the application locally:
  ```python
  flask --app flaskcalculator run --debug
  ```
* Run tests:
  ```python
  pytest
  ```
* Build a coverage report:
  ```python
  coverage run -m pytest
  ```
  # Testing commands
## Addition
* For linux:
    ```
    curl --header "Content-Type: application/json" --request POST --data '{"left_operand":1,"right_operand":1}' http://127.0.0.1:5000/calculator/add
    ```
* For powershell:
    ```
    Invoke-RestMethod -Uri "http://127.0.0.1:5000/calculator/add" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"left_operand":1,"right_operand":1}'
    ```
## History
* For linux:
    ```
    curl --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/calculator/history
    ```
* For powershell:
    ```
    Invoke-RestMethod -Uri "http://127.0.0.1:5000/calculator/history" -Method GET 
    ```