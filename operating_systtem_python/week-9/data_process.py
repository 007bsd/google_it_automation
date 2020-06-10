#!/usr/bin/env python
#
# def to_seconds(hours, mins, secs):
#     return 3600 * hours + 60 * mins + secs
#
#
# print("welcome to time converter")
# cont = "y"
#
# while (cont.lower() == 'y'):
#     hours = int(input("Please enter the hours:\n"))
#     mins = int(input("Please enter the hours:\n"))
#     secs = int(input("Please enter the hours:\n"))
#
#     print("The result {} in seconds".format(to_seconds(hours, mins, secs)))
#     print()
#     cont = input("Do you want to do another conversion? [y to continue] ")
# print("Good bye!")
#
# import os
# print("PATH:" + os.environ.get("HOMEPATH", ""))
# print("Shell: " + os.environ.get("SHELL", ""))
# print("Fruit: " + os.environ.get("FRUIT", ""))
#
# import sys
# print(sys.argv)
#
# import os
# import sys
#
# filename = sys.argv[1]
#
# if not os.path.exists(filename):
#     with open(filename, "w") as f:
#         f.write("new file created\n")
# else:
#     print("Error!, {} file already exit".format(filename))
#     sys.exit(1)
#
# import subprocess
# import os
# subprocess.run(["date"])
# subprocess.run(["sleep", "2"])
#
# my_env = os.environ.copy()
# my_env['PATH'] = os.pathsep.join(["/opt/myapp/", my_env['PATH']])
# result = subprocess.run(["myapp"], env=my_env)

# import sys
# import re
# log_file = sys.argv[1]
#
# with open(log_file) as f:
#     for line in f:
#         if "CRON" not in line:
#             continue
#         pattern = r"USER \((\w+)\)$"
#         line = "The user is USER (naughty_user)"
#         result = re.search(pattern, line)
#         print(result[1])
#

import re
def show_time_of_pid(line):
  pattern = r"(\w+\s+\d+\s\d+:\d+:\d+).*(\[(\d+)\])"
  result = re.search(pattern, line)
  return result[1]+" "+"pid"+":"+result[3]

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
#
# print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
#
# print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
#
# print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
#
# print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
#
# print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
#
# print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
#
# import sys
# import re
# log_file = sys.argv[1]
# usernames = {}
# #name = "good_user"
# #usernames[name]= usernames.get(name, 0) +1
#
# with open(log_file) as f:
#     for line in f:
#         if "CRON" not in line:
#             continue
#         pattern = r"USER \((\w+)\)$"
#
#         result = re.search(pattern, log_file)
#         if result is None:
#             continue
#         name = result[1]
#         usernames[name] = usernames.get(name, 0) + 1
#         print(result[1])
#     print(usernames)


import sys
import re
log_file = sys.argv[1]
usernames = {}
#name = "good_user"
#usernames[name]= usernames.get(name, 0) +1

with open(log_file) as f:
    for line in f:
        if "WARN" not in line:
            continue
        pattern = r"[error]"

        result = re.search(pattern, log_file)
        if result is None:
            continue
        name = result
        usernames[name] = usernames.get(name, 0) + 1
        print(result)
    print(usernames)

