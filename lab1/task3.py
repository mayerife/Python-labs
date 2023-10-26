list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players_in_team = len(list_players) // 2
first_team = list_players[:players_in_team]
second_team = list_players[players_in_team:]

print(first_team)
print(second_team)
