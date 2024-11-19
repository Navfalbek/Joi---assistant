import requests

import config


def get_refreshed_access_token() -> str:
    response = requests.post(
        url='https://accounts.spotify.com/api/token',
        headers={
            'Authorization': 'Basic {}'.format(config.BASE_64)
        },
        data={
            'grant_type': 'refresh_token',
            'refresh_token': config.REFRESH_TOKEN
        }
    )
    if 200 <= response.status_code <= 299:
        response_json = response.json()
        return response_json['access_token']
    else:
        raise Exception('Could not get refreshed token.')
