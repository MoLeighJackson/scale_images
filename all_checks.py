#!/usr/bin/env /c/Users/MoLeigh/AppData/Local/Programs/Python/Python38-32/python

import os
import sys

def check_reboot():
  return os.path.exist("/run/reboot-required")


def main():
  if check_reboo():
    print("Pending reboot.")
    sys.exit(1)

main()
