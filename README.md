# flask-connect-heroku

## Steps
1. run the following commands
    - `brew tap heroku/brew && brew install heroku` (Heroku CLI)
    - `pip3 install gunicorn` (HTTP Web Server Gateway Interface for Python)
    - `pip3 freeze > requirements.txt` (dump all installed packages into **requirements.txt** file)
2. create **Procfile** and add gunicorn
    ```
    web: gunicorn app:app   
    ```
    
    - **web**: web application
    - ...gunicorn **[main-file-name]**:app in this ex, we're using **app.py**
