# использование %
print("В команде Мастера кода участников: %(team1_num)s!" % {'team1_num': 5})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s" % {'team1_num': 5, 'team2_num': 6})

# использование Format
print("Команда Волшебники данных решила задач:{score_2}".format(score_2=42))
print("Волшебники данных решили задачи за {team1_time}c!!".format(team1_time=18015.2))


# использование f строк

def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        'Ничья'
    return result


score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
result = challenge_result(score_1, score_2, team1_time, team2_time)
print(f'Результат битвы: {result}')

print(
    f'Сегодня было решено {int(score_1 + score_2)} задач, в среднем по {(team1_time + team2_time) / (score_1 + score_2):.1f}'
    f' секунды на задачу!')
