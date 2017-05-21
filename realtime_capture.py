#!/usr/bin/python

# imports for observer pattern and scrapping stdout
from observable import Observable
from observer import Observer
import os

# imports for type-observer-view
from testobserverview import TestObserverView

import subprocess, time, os, sys
cmd = ["sudo", "tcpdump", "-c", "5"]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

observable = Observable()

test_observer = TestObserverView()
observable.register(test_observer)

for line in iter(p.stdout.readline, b''):
		observable.update_observers(line.rstrip())

print("program ended")



