# Flask-Project
### After cloning this project, please follow the steps
``` bash
# For Postgres installation please follow this document:
https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart
# After installing Postgres, please read the following documentation for installing pgadmin4:
https://kodemonk.dev/blog/installing-postgresql-on-ubuntu-20-04
# After installing pgadmin4, please create the database which name is  "store", password will be "root", then importing hotel.sql and user.sql

# install requirements.txt
pip3 install -r requirements.txt

# Run project: 
pyhton app.py

#project running URL: http://127.0.0.1:5000/swagger/
```

### Using Tools and Libraries
1. pgAdmin 4
2. Flask
3. psycopg2
4. JWT
5. flask_swagger_ui
6. flask_sqlalchemy

### Project details
This project is crawling the data from website , then those data store into Postgres database.
