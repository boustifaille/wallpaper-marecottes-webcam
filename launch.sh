#!/bin/bash
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$UID/bus

/usr/bin/python3 /home/antho/Documents/code/marecottes/main.py
