from itertools import groupby
import datetime
from dateutil.parser import parse
import re

class Observation:
    reg_observation = "\[([\d -:]+)\] ([\w #]+)"
    reg_guardid = "Guard #([\d]+) "
    guardId = None

    def __init__(self, inp):
        m = re.search(self.reg_observation, inp)
        self.date = parse(m.group(1))
        self.minute = self.date.minute
        action = m.group(2)
        if action.startswith('Guard'):
            m2 = re.search(self.reg_guardid, action)
            self.guardId = m2.group(1)
            self.event = 'start'
        elif action.startswith('falls'):
            self.event = 'sleep'
        elif action.startswith('wakes'):
            self.event = 'awake'

    def __str__(self):
        return "{0} {1} {2}".format(self.guardId, self.date, self.event)

class GuardStats:

    def __init__(self, observations):
        self.observations = observations
        self.guardId = observations[0].guardId
        self.minutesSleeping = [0] * 60

        observations.sort(key=lambda x:str(x.date.month) + '-' + str(x.date.day))
        daily = groupby(observations, lambda x:str(x.date.month) + '-' + str(x.date.day))
        self.dayCount = 0
        awake = 0
        sleep = 0
        for d, obs in daily:
            self.dayCount += 1
            obslist = list(obs)
            l = len(obslist)

            for i in range(l):
                o = obslist[i]
                cnt = 0
                if i + 1 <l:
                    cnt = obslist[i+1].minute - o.minute
                else:
                    cnt = 60 - o.minute
                if o.event == 'awake':
                    awake += cnt
                elif o.event == 'sleep':
                    sleep += cnt
                    for i in range(o.minute, o.minute + cnt):
                        self.minutesSleeping[i] += 1
        self.sleep = sleep
        self.awake = awake

    def __str__(self):
        return "GuardId #{0}: Sleep: {1}, Awake: {2}, Days: {3}, Min: {4}x @{5}.min".format(self.guardId, self.sleep, self.awake, self.dayCount, self.mostFrequentSleep(), self.whenMaxSleep() )

    # new in part 02
    def mostFrequentSleep(self):
        m = max(self.minutesSleeping)
        return m

    def whenMaxSleep(self):
        m = max(self.minutesSleeping)
        minutes = [i for i, j in enumerate(self.minutesSleeping) if j == m]
        return int(minutes[0])

    def getRes(self):
        return int(self.guardId) * self.whenMaxSleep()

if __name__ == "__main__":
    with open("input.txt") as f:
        observations = [Observation(l.strip()) for l in f.readlines()]

    observations.sort(key=lambda x: x.date)

    for obs in observations:

        if obs.guardId is not None:
            id = obs.guardId
        else:
            obs.guardId = id

    observations.sort(key=lambda x: x.guardId)
    grouped_observations = groupby(observations, lambda x: x.guardId)

    guards = []
    for id, obs in grouped_observations:
        g = GuardStats(list(obs))
        guards.append(g)

    g = max(guards,key = lambda x:x.mostFrequentSleep()) # new sort order in part 02
    print('Sleeper:')
    print(g)
    print(g.getRes())
