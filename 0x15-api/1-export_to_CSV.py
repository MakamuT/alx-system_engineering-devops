#!/usr/bin/python3
"""export data in CSV format"""

import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv])
        sys.exit(1)

    user_id = sys.argv[1]
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    res_user = requests.get(url_user)

    if res_user.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_name = res_user.json().get('username')
    url_tasks = f'{url_user}/todos'
    res_tasks = requests.get(url_tasks)

    if res_tasks.status_code != 200:
        print("Error fetching tasks")
        sys.exit(1)

    tasks = res_tasks.json()

    csv_filename = f'{user_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csv_writer.writerow([user_id, user_name, completed, title_task])
