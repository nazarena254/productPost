# Flaskshop

## Description
Basic flask application that enables users to sign in and post their products for selling.

## Author
Nazarena Wambura.</br>
[Github](https://github.com/nazarena254/)

## Technologies used
* Python3.9
* Flask2.1.1
* Heroku7.60.2


### Running the Application
1. Pre-requisites
   - Ensure to activate virtual environment called virtual,using:
     - source virtual/bin/activate
   - Install flask and pip
   - Install flask_script

2. Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app ('development')
3. Add the export configurations in a start.sh
   - export SECRET_KEY= "Your secret key"
   - export API_KEY= "Your Api key" if used
4. Run using the executable file ,with command :
   - ./start.sh

## Contact Information
Email:<nancyngunjiri1@gmail.com>

### License

[MIT License]
<!-- (https://github.com/MugeraH/flask_code/blob/main/license) -->
Copyright (c) 2022
