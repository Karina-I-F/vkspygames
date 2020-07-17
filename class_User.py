import requests
import time


class User:
    def __init__(self, user_id, TOKEN):
        self.TOKEN = TOKEN
        if str(user_id).isdigit():
            self.USER_ID = user_id
        else:
            self.params = {
                'access_token': self.TOKEN,
                'v': '5.104',
                'screen_name': user_id
            }
            response = requests.get('https://api.vk.com/method/utils.resolveScreenName', params=self.params).json()
            print('.')
            self.USER_ID = response['response']['object_id']
        self.params = {
            'access_token': self.TOKEN,
            'v': '5.104',
            'user_id': self.USER_ID
        }

    def get_groups(self):
        self.params['extended'] = 1
        self.params['fields'] = 'members_count'
        time.sleep(1)
        response = requests.get('https://api.vk.com/method/groups.get', params=self.params).json()
        print('.')
        return response

    def get_strip_groups_list(self):
        groups_list = [item['id'] for item in User.get_groups(self)['response']['items']]
        print('.')
        return groups_list

    def get_friends_ids(self):
        response = requests.get('https://api.vk.com/method/friends.get', params=self.params).json()
        print('.')
        id_set = [item for item in response['response']['items']]
        return id_set
