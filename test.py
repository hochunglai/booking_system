import threading


def worker(num):
    """Thread worker function"""
    print(f"Worker {num} started")
    # Do some work here...
    print(f"Worker {num} finished")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
