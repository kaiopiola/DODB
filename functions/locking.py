import fcntl

# Function to get a file locked
def lock_file(file):
    fcntl.flock(file.fileno(), fcntl.LOCK_EX)

# Function for unlocking a file
def unlock_file(file):
    fcntl.flock(file.fileno(), fcntl.LOCK_UN)
