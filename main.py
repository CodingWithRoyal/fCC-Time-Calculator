# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time, add_hrs
from unittest import main


print(add_time("9:15 PM", "5:30"))

# print(add_hrs(2, 13, "PM"))


# Run unit tests automatically
main(module='test_module', exit=False)