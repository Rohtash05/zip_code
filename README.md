# Documentation
# Description
This application can be used to calculate the zip code of any city by filtering through the country, state, and city.

# Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

```bash
pip install -r requirements.txt
```

You can use virtualenv or you can run directly


# Run
Use `flask run` to run the flask application.
To use it outside the network you need to set 
`FLASK_RUN_HOST=0.0.0.0` or `host of the server`

OR 

You can run the application by running `run.sh` file. If you are using virtualenv you need to activate the environment first before starting the application.

# Database
The database file used is an SQLite database and is available at `db/zip_code.db`.


# How to use
**Note:- Base URL is `https://<host>`. Replace `<host>` by your host or localhost if you running in a local environment.** 
- You can browse all the countries by `base_url/country` endpoint.
    - For Example: `http://localhost:5000/country`
- You can request all states of the selected country by `base_url//state/<country_id>`
    - For Example: `http://localhost:5000/state/in`
- You can request all cities of the selected state by `base_url//state/<country_id>/<state_id>`
    - For Example: `http://localhost:5000/state/in/punjab`
- You can request zip of the selected city by `base_url//state/<country_id>/<state_id>/<city_id>`
    - For Example: `http://localhost:5000/state/in/punjab/behram`