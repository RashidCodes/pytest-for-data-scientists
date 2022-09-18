 # topologicalsorter 
from graphlib import TopologicalSorter
from queue import SimpleQueue
from random import randint
import time 
import logging


logging.basicConfig(format="[%(levelname)s][%(asctime)s][%(filename)s]: %(message)s", level=logging.INFO) 




task_queue = SimpleQueue()

finalised_task_queue = SimpleQueue()


# think of a task as a node 
def run_task(task_name: str = 'A', eta: int = 1):
    # perform some work 
    logging.info(f"Task {task_name}: Working for {eta} seconds")
    time.sleep(eta)
    logging.info(f"Done running task {task_name}")
    



# a worker processes tasks and places the task 
# on the finalized_task_queue
def worker():

    # place tasks on the finalized queue after processing 
    logging.info(f"Dequeueing tasks from task_queue")

    while task_queue.qsize() != 0:

        task = task_queue.get()

        # run the task 
        eval(f"run_task(task, randint(1, 3))") 

        # place the task in the finalized queue 
        finalised_task_queue.put(task)

    logging.info(f"Deque complete!")


    


    

# the keys are the nodes 
# the values are iterables of all predecessors of that node in the graph
graph = {'D': {'B', 'C'}, 'C': {'A'}, 'B': {'A'}}

    
ts = TopologicalSorter(graph)

# immediate sorting of the nodes in the graph
# tuple(ts.static_order())

# prepare the graph 
ts.prepare() 

while ts.is_active():

    # at some point, get_ready() will return 0 nodes 

    for node in ts.get_ready():
        logging.info(f"Placing node: {node} on task queue")
        task_queue.put(node) 


    # start your worker 
    worker()

    node = finalised_task_queue.get() 

    # mark the node as done 
    ts.done(node)
     
