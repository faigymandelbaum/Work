# Was done with no hints.
import multiprocessing
import time

tasks = ['Wash laundry', 'Wash dishes', 'Babysit the kids', 'Cook supper', 'Put on linen', 'Call Bubby', 'Buy milk', 'Sooth the baby', 'Fold laundry', 'Vacume carpets', 'Clean the windows', 'Boil hot water']

def run_task(*task):
    for t in task:
        print (t)

if __name__ == '__main__':

    task1 = multiprocessing.Process(target = run_task, args = tasks[:3])
    task2 = multiprocessing.Process(target = run_task, args = tasks[3:6])
    task3 = multiprocessing.Process(target = run_task, args = tasks[6:9])
    task4 = multiprocessing.Process(target = run_task, args = tasks[9:])
    task1.start()
    task2.start()
    task3.start()
    task4.start()

    task1.join()
    task2.join()
    task3.join()
    task4.join()

# Because all functions are running at once it can come up in a different order! 

