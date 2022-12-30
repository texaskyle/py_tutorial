import threading
import time

"""def breakfast():
    time.sleep(3)
    print("You have finished eating breakfast")


def study():
    time.sleep(5)
    print("You have finished doing the assignment")


def prepare():
    time.sleep(2)
    print("You have dressed nicely!")

# breakfast()
# study()
# prepare()


x = threading.Thread(target=breakfast, args=())
x.start()

y = threading.Thread(target=study, args=())
y.start()

z = threading.Thread(target=prepare, args=())
z.start()

# thread synchronization
x.join()
y.join()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())"""


# daemon thread

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(2)
        count += 1
        print(f"You are logged in for {count} seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

input("Do you wish to quit? ")
