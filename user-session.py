from datetime import datetime, timedelta
timeout = timedelta(minutes=30)
sessions = {}
with open('c:\\temp\events.txt', 'r') as infile:
    for line in infile:
        print(line.strip().split(','))
        uid, dt = line.strip().split(',')
        eventTime = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
        if uid not in sessions:
            sessions[uid] = {1: [eventTime, eventTime, 1]}
        else:
            userSessions = sessions[uid]
            userSessionCount = len(userSessions)
            lastEventTime = userSessions[userSessionCount][1]
            if eventTime - lastEventTime > timeout:
                userSessionCount += 1
                userSessions[userSessionCount] = [eventTime, eventTime, 1]
            else:
                userSessions[userSessionCount][2] += 1
                userSessions[userSessionCount][1] = eventTime

print('user_id session_id session_start session_end activity_count')
for uid, ss in sessions.items():
    for sid, s in ss.items():
        print(uid, sid, s[0].isoformat(), s[1].isoformat(), s[2])