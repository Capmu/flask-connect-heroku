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
3. implement python script to add API(s), ex: app.py in this repository
4. push this to a remote repository
5. deploy to Heroku
    - run `heroku login` (it'll automatically open browser to login to Heroku)
    - change directory to the repository
    - run `heroku create <new-app-name>` (create new app name in Heroku)
    - run `git push heroku <branch-name>` (to deploy the Flask app)
