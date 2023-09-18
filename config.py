import os


DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'localhost',
            'DB_PORT': '3306',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_PWD' : os.environ.get('SOURCE_DB_PWD')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_PORT': '5432',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('TARGET_DB_USER'),
            'DB_PWD' : os.environ.get('TARGET_DB_PWD')
        }
    }
}