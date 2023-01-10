import random
import csv
import pandas


def match_birthdays(dupe_list, selected_birthdays):
    duplicate_birthdays = dict()
    for dupe in dupe_list:
        for key, value in selected_birthdays.items():
            if value == dupe:
                duplicate_birthdays[key] = value
    return duplicate_birthdays


def find_birthday_matches(birthday_list, num):
    birthdays_indexed = list(birthday_list.items())
    selected_birthdays = dict()
    numbers_used = []
    top_range = num + 1
    for i in range(1, top_range):
        rand_num = random.randint(0, 999)
        while rand_num in numbers_used:
            rand_num = random.randint(0, 999)
        numbers_used.append(rand_num)
        selected_birthdays[birthdays_indexed[rand_num][0]] = birthdays_indexed[rand_num][1]

    birthdays_set = set()
    dupe_birthdays = []
    dupe_birthdays_found = dict()
    for checkPerson in selected_birthdays:
        if selected_birthdays[checkPerson] not in birthdays_set:
            birthdays_set.add(selected_birthdays[checkPerson])
        else:
            dupe_birthdays.append(selected_birthdays[checkPerson])

    if len(dupe_birthdays) > 0:
        dupe_birthdays_found = match_birthdays(dupe_birthdays, selected_birthdays)

    return dupe_birthdays_found


birthdays = dict()
with open("\\fillmore\\BI_Support_SSIS\\birthday_list.txt", "r") as namesFile:
    birthday_reader = csv.DictReader(namesFile, delimiter='\t')
    for person in birthday_reader:
        birthdays[person['name']] = person['birthday']

dupe_lists = []
times_dupes_found = 0
tabular_data = {"num_people": [], "percent_match": []}
num_iterations = 100
group_size = 23
for j in range(group_size, 100):
    for k in range(1, num_iterations + 1):
        dupe_birthdays = find_birthday_matches(birthdays, group_size)
        if len(dupe_birthdays) > 0:
            times_dupes_found += 1
            dupe_lists.append(dupe_birthdays)
    match_percent = round((times_dupes_found / num_iterations) * 100)
    tabular_data["num_people"].append(group_size)
    tabular_data["percent_match"].append(match_percent)

    dupe_lists = []
    times_dupes_found = 0
    group_size += 1

birthdays_collisions = pandas.DataFrame(tabular_data)
