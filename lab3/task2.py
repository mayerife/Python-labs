def find_common_participants(first_group, second_group, delimiter=','):
    first_group_list = first_group.split(delimiter)
    second_group_list = second_group.split(delimiter)

    common_participants = list(set(first_group_list).intersection(set(second_group_list)))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)
