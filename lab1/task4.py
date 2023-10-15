users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

stat = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

total_users = len(users)
unique_users = len(set(users))
stat["Общее количество"] = total_users
stat["Уникальные посещения"] = unique_users

print(stat)
