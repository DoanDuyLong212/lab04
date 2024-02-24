open('sales.txt', 'w')

import datetime
now = datetime.datetime.now()
file_name = now.strfime('%Y-%m-%d_%H-%M-%S') + '.txt'
open('file_name', 'w')

import os

file_path = "example.txt"

# Define the permissions in octal format (e.g., 0o644 for user read/write, others read-only)
permissions = 0o644

with os.open(file_path, os.O_CREAT | os.O_EXCL, permissions) as f:
    pass