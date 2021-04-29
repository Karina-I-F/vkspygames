import requests
from time import sleep


class User:
    def __init__(self, user_id, TOKEN):
        self.TOKEN = TOKEN
        self.user_id = user_id

    def __request(self, url, params):
        sleep(0.35)
        response = requests.get(url, params=params)
        print('.')
        if response.status_code != 200:
            print('Error')
            return None
        return response.json()

    def get_params(self, add_params: dict = None):
        params = {
            'access_token': self.TOKEN,
            'v': '5.104'
        }
        if add_params:
            params.update(add_params)
            pass
        return params

    def check_user_id(self):
        if str(self.user_id).isdigit():
            self.USER_ID = self.user_id
        else:
            params = self.get_params()
            params['screen_name'] = self.user_id
            response = self.get_request('utils.resolveScreenName', params)
            self.USER_ID = response['response']['object_id']
        params = self.get_params()
        params['user_id'] = self.USER_ID
        return params

    def get_request(self, method, params):
        response = self.__request(f'https://api.vk.com/method/{method}',
                                  params)
        return response

    def get_groups(self):
        params = self.check_user_id().copy()
        params['extended'] = 1
        params['fields'] = 'members_count'
        response = self.get_request('groups.get', params)
        return response

    def get_strip_groups_list(self):
        groups_list = [item['id'] for item in self.get_groups()['response']['items']]
        return groups_list

    def get_friends_ids(self):
        response = self.get_request('friends.get', self.check_user_id())
        id_set = [item for item in response['response']['items']]
        return id_set
