SUCCESS = {
    'COUNTRY_LIST_SUCCESS' : {
        'status_code':200,
        'success': True,
        'type':'COUNTRY_LIST_SUCCESS',
        'message':'Country List Sent Successfully',
        'data':None
    },
     'STATE_LIST_SUCCESS' : {
        'status_code':200,
        'success': True,
        'type':'STATE_LIST_SUCCESS',
        'message':'State List Sent Successfully',
        'data':None
    },
    'CITY_LIST_SUCCESS' : {
        'status_code':200,
        'success': True,
        'type':'CITY_LIST_SUCCESS',
        'message':'Cities List Sent Successfully',
        'data':None
    },
    'ZIP_CODE_SUCCESS' : {
        'status_code':200,
        'success': True,
        'type':'ZIP_CODE_SUCCESS',
        'message':'ZIP Code Sent Successfully',
        'data':None
    },
}

ERROR = {
    'INTERNAL_SERVER_ERROR' : {
        'status_code':500,
        'success': False,
        'type':'INTERNAL_SERVER_ERROR',
        'message':'INTERNAL_SERVER_ERROR',
    },
    'INVALID_INPUT' : {
        'status_code':400,
        'success': False,
        'type':'INVALID_INPUT',
        'message':'Please send valid input data',
    },
    'COUNTRY_LIST_EMPTY' : {
        'status_code':404,
        'success': False,
        'type':'COUNTRY_LIST_EMPTY',
        'message':'There are no countries in this list.',

    },
    'NO_STATE' : {
        'status_code':404,
        'success': False,
        'type':'NO_STATE',
        'message':'There are no state for the selected country in our database',

    },
    'NO_CITY' : {
        'status_code':404,
        'success': False,
        'type':'NO_CITY',
        'message':'There are no city for the selected country and state in our database',

    },
    'NOT_FOUND' : {
        'status_code':404,
        'success': False,
        'type':'NOT_FOUND',
        'message':'ZIP code not Available',

    }
}