template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
        },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int,
            },
        'birthplace': {
            'country': str,
            'city': str
            },
        }
    }

john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
        },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27,
            },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
            },
        }
    }

eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
        },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29,
            },
        'birthplace': {
            'country': 'United Kingdom'
            },
        }
    }

michele = {
    'user_id': 102,
    'name': {
        'first': 'Michele',
        'last': 'Palin'
        },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5,
            },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Shiffield'
            },
        }
    }

def check_structure(data: dict, template: dict):
    state = True
    text = 'Ok'
    if data.keys() == template.keys():
        for key, value in data.items():
            if not state:
                return state, text
            if hasattr(value, '__iter__') and not isinstance(value, str):
                state, text = check_structure(value, template[key])
            else:
                if type(data[key]) != template[key]:
                    state = False
                    text = 'Wrong Type'
    else:
        state = False
        text = 'Missing Keys'
    return state, text

if __name__ == '__main__':
    print(check_structure(michele, template))