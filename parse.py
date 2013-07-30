#!/usr/bin/env python
#Version $Revision: 1.2 $
#author len@len.ro

#borrowed from http://www.len.ro/work/skype-logs-archiving-on-linux/


import re, sys, os
 
file=sys.argv[1]
user=sys.argv[2]
logbase=sys.argv[3]
 
cnt = 0
 
hist = {}
hist['nobody'] = []
 
for line in open(file, 'r').readlines():
    msg = {}
    parts = line.split('|')
    for p in parts:
        m = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}\:[0-9]{2}\:[0-9]{2}', p)
        if m:
            date = m.group(0)
            msg['date'] = date
        else:
            i=p.find(':')
            key = p[:i].strip()
            val = p[i+1:].strip()
            msg[key] = val
            if key == 'Session':
                m = re.search('#([0-9a-zA-Z._-]+)/\$([0-9a-zA-Z._-]+);', val)
                if m:
                    u1 = m.group(1)
                    u2 = m.group(2)
                    if u1 == user:
                        msg['other'] = u2
                    if u2 == user:
                        msg['other'] = u1
                else:
                    print 'Error parsing session:', val
 
    #print msg
 
    if msg.has_key('other'):
        other = msg['other']
        if not hist.has_key(other):
            hist[other] = []
        hist[other].append(msg)
    else:
        hist['nobody'].append(msg)
    cnt = cnt + 1
 
for k in hist:
    #print date
    s_hist = sorted(hist[k], key = lambda hist: hist['date'])
    last_day = None
    current_log = None
    for e in s_hist:
        if e.has_key('date'):
            day = e['date'][:10]
            #print day, last_day
            if last_day == None or last_day != day:
                last_day = day
                try:
                    os.makedirs(logbase+'/'+k)
                except:
                    pass
                log_name = '%s/%s/%s.log' % (logbase, k, day)
                #print log_name
                if current_log != None:
                    current_log.close()
                if not os.path.exists(log_name):
                    current_log = open(log_name, 'w')
                else:
                    current_log = None
            if current_log != None:
                if e.has_key('Message'):
                    current_log.write('(%s) %s: %s\n' %(e['date'], e['Sender'], e['Message']))
                else:
                    current_log.write(e['date'] + ': -\n')
