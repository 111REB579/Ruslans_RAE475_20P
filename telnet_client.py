#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import telnetlib #izmantotā bibliotēka

HOST = '127.0.0.1' #attālinātais serveris
PORT = 10023 #ports
timeout = 100 #savienojuma laiks

tn = telnetlib.Telnet(HOST, PORT) #interfeisa definēšana
tn.set_debuglevel(100) #kļūdu līmenis
data = tn.read_until("custom server", timeout=1) #parametra definēšana
print "Data: " + data #datu izvade

tn.close() #interfeisa noslēgšāna
