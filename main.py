import concurrent.futures
import queue
import time

class WorkQueue(queue.Queue):
    def __init__(self):
        super().__init__()

    def steal(self):
        try:
            task = self.get(block=False)
            return task
        except queue.Empty:
            return None

def heavy_task():
    result = sum(range(10**7))
    return result

def worker(worker_id, work_queue, result_queue):
    while True:
        try:
            task = work_queue.get(block=False)
        except queue.Empty:
            task = work_queue.steal()

        if task is None:
            break

        if task == "steal":
            print(f"Worker {worker_id} is stealing a task...")
            result_queue.put(f"Worker {worker_id} stole a task.")
            continue

        result = task()
        result_queue.put(result)

def main():
    work_queue = WorkQueue()
    result_queue = queue.Queue()

    num_tasks = 10
    for _ in range(num_tasks):
        work_queue.put(heavy_task)

    work_queue.put("steal")

    num_workers = 4
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(worker, i, work_queue, result_queue) for i in range(num_workers)]

        concurrent.futures.wait(futures)

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print("Results:", results)

if __name__ == "__main__":
    main()
