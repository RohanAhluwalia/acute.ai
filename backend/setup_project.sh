#!/bin/bash

mkdir -p my_diabetes_app/app/{api/v1/endpoints,core,models,db,crud,schemas}
touch my_diabetes_app/app/{__init__.py,main.py}
touch my_diabetes_app/app/api/{__init__.py}
touch my_diabetes_app/app/api/v1/{__init__.py}
touch my_diabetes_app/app/api/v1/endpoints/{__init__.py,health.py,users.py,data.py}
touch my_diabetes_app/app/core/{__init__.py,config.py}
touch my_diabetes_app/app/models/{__init__.py,user.py,data.py}
touch my_diabetes_app/app/db/{__init__.py,base.py,session.py}
touch my_diabetes_app/app/crud/{__init__.py,crud_user.py,crud_data.py}
touch my_diabetes_app/app/schemas/{__init__.py,user.py,data.py}
touch my_diabetes_app/{Dockerfile,docker-compose.yml,requirements.txt,.env}

echo "Project structure created successfully!"
