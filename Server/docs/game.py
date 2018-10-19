# -*- coding: utf-8 -*-

from . import parameter
EASY_LEVEL = {
    'tags': ['Game'],
    'description': 'easy level',
    'parameters': [
        parameter('reqWord', '단어'),
        parameter('time', '시간'),
        parameter('number', '번호', 'json', 'int')
    ],
    'responses': {
        '200': {
            'description': '다음 단어 보냄',
            'examples': {
                '': [
                    True,
                    '단어'
                ]
            }
        },
        '406': {
            'description': '올바르지 않은 단어'
        }
    }
}

EASY_START = {
    'tags': ['Game'],
    'description': 'easy-level-start',
    'responses': {
        '200': {
            'description': '첫 단어 보냄'
        }
    }
}

HARD_LEVEL = {
    'tags': ['Game'],
    'description': 'hard level',
    'parameters': [
        parameter('reqWord', '단어'),
        parameter('time', '시간'),
        parameter('number', '번호')
    ],
    'responses': {
        '200': {
            'description': '다음 단어 보냄'
        },
        '406': {
            'description': '올바르지 않은 단어'
        }
    }
}

HARD_START = {
    'tags': ['Game'],
    'description': 'hard-level-start',
    'responses': {
        '200': {
            'description': '첫 단어 보냄'
        }
    }
}
