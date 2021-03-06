# -*- coding: utf-8 -*-

"""Part 1 : Setup index"""

dict = {}  # a emtry dictionary.
n = 100
for row in range(0, n):

    information = input()

    line_words = information.split()
    # split the information inputed into lines by '/n'

    for word in line_words:  # Judge every word in every lines .

        # If the word appear first time .
        if word not in dict:
            item = set()  # set up a new set .
            item.add(row + 1)  # now rows
            dict[word] = item  # Add now rows into keys(item).

        # THe word have appeared before .
        else:
            dict[word].add(row + 1)  # Add now rows into keys(item).

# print(dict)    we can get the information dictionary.


'''Part 2 : Print index'''

word_list = dict.items()  # Get dict's items .

word_list.sort(key=lambda items: items[0])  # Sort by word in dict.

for word, row in word_list:  # Ergodic word and row in word_list .

    list_row = list(row)
    list_row.sort()

    # Change int row into string row .
    for i in range(0, len(list_row)):
        list_row[i] = str(list_row[i])

    # print result the part 2 needed .
    print(word + ':', ', '.join(list_row))

''' Part 3 : Query '''


# define judger to judger if all querys are in dict.
def judger(dict, query):
    list_query = query.split()
    for word in list_query:
        if word not in dict:
            return 0  # for every query ,if there is one not in dict,return 0
    return 1  # all query in dict .


query_list = []

# for input , meet '' ,stop input.
while True:
    query = input()
    if query == '':
        break
    elif len(query) != 0:
        query_list.append(query)  # append query inputed to a list query_list .

# Ergodic every query in query_list.
for list_query in query_list:

    # if judger return 0.
    if judger(dict, list_query) == 0:
        print('None')

    else:
        list_query = list_query.split()
        query_set = set()  # get a empty set

        # union set to get rows .
        for isquery in list_query:
            query_set = query_set | dict[isquery]

        # intersection to get common rows .
        for isquery in list_query:
            query_set = query_set & dict[isquery]

        # if intersection == 0
        if len(query_set) == 0:
            print('None')

        else:
            query_result = list(query_set)
            query_result.sort()
            for m in range(len(query_result)):
                query_result[m] = str(query_result[m])

            print(', '.join(query_result))
