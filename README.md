# Flask-Project
### After cloning this project, please follow the steps
``` bash
# For Postgres installation please follow this document:
https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart
# After installing Postgres, please read the following documentation for installing pgadmin4:
https://kodemonk.dev/blog/installing-postgresql-on-ubuntu-20-04
# After installing pgadmin4, please create the database which name is  "store", password will be "root", then importing hotel.sql and user.sql

# Install virtual environment
pip3 install virtualenv

#Create a virtual environment
virtualenv venv (you can use any name insted of venv)

#Active your virtual environment
source venv/bin/activate

# Install requirements.txt
pip3 install -r requirements.txt

# Run project: 
pyhton app.py

#Project running URL: http://127.0.0.1:5000/swagger/
```

### Using Tools and Libraries
1. pgAdmin 4
2. Flask
3. psycopg2
4. JWT
5. flask_swagger_ui
6. flask_sqlalchemy

### Project details
This project is a API based on Flask. In order to use the API, the users have to sign up first then to generate the API key users need to sign in. Every API keys have 40 seconds of validity. After exiting 40 seconds to generate a new API key user need to sign in again.
