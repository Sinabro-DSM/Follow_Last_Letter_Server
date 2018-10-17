# -*- coding: utf-8 -*-

import os


class Config:
    SERVICE_NAME = 'follow-last-letter'

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,
        'info': {
            'title': SERVICE_NAME + ' API',
            'version': 1.0,
            'description': ''
        },
        'host': 'localhost',
        'basePath': '/'
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Game',
                'description': '게임 관련 API'
            }
        ]
    }