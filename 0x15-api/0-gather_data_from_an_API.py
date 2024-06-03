#!/usr/bin/python3
"""employee data from API"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
   if len(sys.argv) > 1:
      if re.fullmatch(r'\d+', sys.argv[1]):
         id = int(sys.argv[1])
         request = requests.get('{}/users/{}'.format(REST_API, id)).json()
         task_request = requests.get('{}/todos'.format(REST_API)).json()
         employee_name = request.get('name')
         tasks = list(filter(lambda x: x.get('userID') == id, task_request))
         completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
         print(
              'Employee {} is done with taks({}/{}):'.format(
		emp_name,
		len(completed_tasks),
		len(tasks)
		)
	)
      if len(completed_tasks) > 0:
	 for task in completed_tasks:
	     print('\t {}'.format(task.get('title')))
