# Shortcut Name: Lock Screen
# Shortcut Key: Alt+L 

from threading import Timer
from gi.repository import Notify

import subprocess
import time

def lockScreen():
	subprocess.check_output(["gnome-screensaver-command", "-l"])

def notify():
	Notify.init("Lock Screen")
	Notify.Notification.new("Lock Screen", "2 minutes remaining.").show()

Notify.init("Lock Screen")
Notify.Notification.new("Lock Screen", "Starting...").show()

twoMinutes = 2 * 60;
lockScreenTime = 2.5 * 60 * 60 - twoMinutes;

time.sleep(lockScreenTime)
notify()
time.sleep(twoMinutes)
lockScreen()