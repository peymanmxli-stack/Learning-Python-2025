# Rank 1
with open("task.txt", "w") as f:
    f.write("Context Manager Task")

# Rank 2
with open("task.txt", "r") as f:
    print(f.read())

# Rank 3
class MyContext:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")

# Rank 4
with MyContext():
    print("Inside context")

# Rank 5
class LoggerContext:
    def __enter__(self):
        print("Process started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Process ended")

with LoggerContext():
    print("Running process")
