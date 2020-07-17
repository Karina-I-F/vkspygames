import json
from class_User import User

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
user_id = input('Введите id пользователя: ')


def get_uncommon_groups(user_id):
    main_user = User(user_id, TOKEN)
    friends_set = main_user.get_friends_ids()
    groups_ids = main_user.get_strip_groups_list()
    counter = 1
    print('Идёт проверка друзей и их групп:')
    for freind_id in friends_set:
        user = User(freind_id, TOKEN)
        try:
            new_groups_list = user.get_strip_groups_list()
        except KeyError:
            print(f'Профиль пользователя с id {freind_id} приватный или был заблокирован.')
            print(f'Обработано {counter}/{len(friends_set)}')
            counter += 1
            continue
        groups_ids = set(groups_ids) - set(new_groups_list)
        print(f'Обработано {counter}/{len(friends_set)}')
        counter += 1
    return groups_ids


def get_data(user_id):
    data = []
    user = User(user_id, TOKEN)
    unique_groups = get_uncommon_groups(user_id)
    for group in user.get_groups()['response']['items']:
        if group['id'] in unique_groups:
            try:
                data.append({'name': group['name'], 'gid': group['id'], 'members_count': group['members_count']})
            except KeyError:
                continue
    return data


def dump_json(user_id):
    with open('groups.json', 'w', encoding='utf-8') as file:
        json.dump(get_data(user_id), file, ensure_ascii=False)


dump_json(user_id)
