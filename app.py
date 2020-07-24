import os
import sqlite3
from flask import Flask
from constants import SUCCESS, ERROR


app = Flask(__name__)


@app.route('/country', methods=['GET'])
def country():
    try:
        all_countries = []
        conn = sqlite3.connect('db/zip_code.db')
        cur = conn.execute('select distinct country_code from zip_codes;')
        rows = cur.fetchall()
        all_countries = [row[0] for row in rows]
        if len(all_countries) == 0:
            return ERROR['COUNTRY_LIST_EMPTY'],ERROR['COUNTRY_LIST_EMPTY']['status_code']
        res = SUCCESS['COUNTRY_LIST_SUCCESS']
        res['data'] = all_countries
        return res
    except Exception as e:
        return ERROR['INTERNAL_SERVER_ERROR'],ERROR['INTERNAL_SERVER_ERROR']['status_code']
   
   

@app.route('/state/<country_id>')
def get_state(country_id):
    try:
        if ';' in country_id:
            return ERROR['INVALID_INPUT'],ERROR['INVALID_INPUT']['status_code']
        all_states = []
        if not country_id:
            return ERROR['NO_STATE'],ERROR['NO_STATE']['status_code']
        conn = sqlite3.connect('db/zip_code.db')
        query = f"select distinct state from zip_codes where LOWER(country_code)=LOWER('{country_id}')"
        cur = conn.execute(query)
        rows = cur.fetchall()
        all_states = [row[0] for row in rows]
        if len(all_states)  == 0:
            return ERROR['NO_STATE'],ERROR['NO_STATE']['status_code']
        res = SUCCESS['STATE_LIST_SUCCESS']
        res['data'] = all_states
        return res
    except Exception as e:
        return ERROR['INTERNAL_SERVER_ERROR'],ERROR['INTERNAL_SERVER_ERROR']['status_code']

@app.route('/city/<country_id>/<state_id>/')
def get_city(country_id, state_id):
    try:
        if ';' in country_id or ';' in state_id:
            return ERROR['INVALID_INPUT'],ERROR['INVALID_INPUT']['status_code']

        all_cities = []
        if not state_id:
            return ERROR['NO_CITY'],ERROR['NO_CITY']['status_code']
        conn = sqlite3.connect('db/zip_code.db')
        query = f"select distinct place_name from zip_codes where LOWER(state)=LOWER('{state_id}') AND LOWER(country_code)=LOWER('{country_id}')"
        cur = conn.execute(query)
        rows = cur.fetchall()
        all_cities = [row[0] for row in rows]
        if len(all_cities)  == 0:
            return ERROR['NO_CITY'],ERROR['NO_CITY']['status_code']
        res = SUCCESS['CITY_LIST_SUCCESS']
        res['data'] = all_cities
        return res
    except Exception as e:
        return ERROR['INTERNAL_SERVER_ERROR'],ERROR['INTERNAL_SERVER_ERROR']['status_code']

@app.route('/zip_code/<country_id>/<state_id>/<city_id>')
def get_zip_code(country_id, state_id,city_id):
    try:
        if ';' in country_id or ';' in state_id or ';' in city_id:
            return ERROR['INVALID_INPUT'],ERROR['INVALID_INPUT']['status_code']
        conn = sqlite3.connect('db/zip_code.db')
        query = f"select distinct postal_code from zip_codes where LOWER(state)=LOWER('{state_id}') AND LOWER(country_code)=LOWER('{country_id}') AND LOWER(place_name)=LOWER('{city_id}')"
        print(query)
        cur = conn.execute(query)
        zip_code = cur.fetchone()
        if len(zip_code) == 0:
            return ERROR['NOT_FOUND'],ERROR['NOT_FOUND']['status_code']
        res = SUCCESS['ZIP_CODE_SUCCESS']
        res['data'] = zip_code[0]
        return res
    except Exception as e:
        print(e)
        return ERROR['INTERNAL_SERVER_ERROR'],ERROR['INTERNAL_SERVER_ERROR']['status_code']

app.run()