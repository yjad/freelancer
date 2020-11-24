"""
I am new to constraint programming and try to figure out how to solve my problem. 
I have 3 workers. 
They have 5 jobs with different times. 
Workers should go from home to each work and finish it at first, then go to the next jobs. 
Some jobs have priority over other jobs. 
They work 5 days a week and go back home and come back next week. 
The objective function is to minimize the distance (Workers have different homes). 
Could you guide me on how to assign tasks to workers
"""

import sqlite3
from DB import get_tasks

workers=[{'w_id': 1, 'home_dist':30}, 
        {'w_id': 2, 'home_dist':20},
        {'w_id': 3, 'home_dist':50}]
jobs = [{'job_id':1, 'prio':1, 'MD': 5}, 
        {'job_id':2, 'prio':2, 'MD': 10}, 
        {'job_id':3, 'prio':3, 'MD': 20},
        {'job_id':4, 'prio':4, 'MD': 6}, 
        {'job_id':5, 'prio':3, 'MD': 23}]
        
assign = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]


tasks = get_tasks()

total_distance = 0
total_md = 0
for task in tasks:
    total_md = total_md + task[2]
  
for worker in workers:  
    worker_distance = total_md / 5 * (worker['home_dist'] * 2)
    worker_distance = total_md / 5 * (worker['home_dist'] * 2)
    print (f"Worker: {worker['w_id']}, MD: {total_md}, distance: {worker_distance}, home distance: {worker['home_dist']}") 
