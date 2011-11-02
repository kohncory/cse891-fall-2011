import csv, urllib

def load_csv(url):
    d = {}
    fp = urllib.urlopen(url)
    for row in csv.DictReader(fp):
        key = row['date']
        value = row['fish']

        x = d.get(key, [])
        x.append(value)
        d[key] = x
    return d


def make_dates_dict(fish_d):
    dates_d = {}
    for date in fish_d:
        fish_list = list(fish_d[date])
        for i in range(len(fish_list)):
            # starting with the first fish eaten on every day
            fish = fish_list[i]
            # get a list of dates with that fish already assigned; create a new list if none seen yet.
            date_list = dates_d.get(fish, [])
            # append the date to the list
            date_list.append(date)
            temp = set(date_list)
            date_list = list(temp)
            date_list.sort()
            # and re-restore it in the dictionary
            dates_d[fish] = date_list
    return dates_d


def get_fishes_by_date(fish_d, date):
    global fishlist
    if date in fish_d.keys():
        fishlist = fish_d[date]
    else:
        fishlist = []
    return fishlist


def get_dates_by_fish(dates_d, fish):
    global datelist
    if fish in dates_d.keys():
        datelist = dates_d[fish]
    else:
        datelist = []
    return datelist


def get_fishes_by_datelist(fish_d, datelist):
    global datelistdict
    datelistdict = {}
    for date in datelist:
        datelistdict[date] = get_fishes_by_date(fish_d, date)
    return datelistdict


def get_dates_by_fishlist(dates_d, fishlist):
    global fishlistdict
    fishlistdict = {}
    for fish in fishlist:
        fishlistdict[fish] = get_dates_by_fish(dates_d, fish)
    return fishlistdict
        


fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
dates_d = make_dates_dict(fish_d)

get_fishes_by_date(fish_d, '1/2')
get_dates_by_fishlist(dates_d, fishlist)

get_dates_by_fish(dates_d, 'plaice')
get_fishes_by_datelist(fish_d, datelist)


numfishondatedict = {}
for date in datelistdict:
    numfishondatedict[date] = len(datelistdict[date])


numfishdict = {}
for num in set(numfishondatedict.values()):
    numfishdict[num] = 0
    for n in numfishondatedict.values():
        if num == n:
            numfishdict[num] += 100./len(numfishondatedict.values())

print numfishdict


#############################

import random
from matplotlib import pyplot
import dhtml
image_file = dhtml.join_path(crunchy.temp_dir, "graph.png")

pyplot.clf()

pyplot.figure(1, figsize=(6,6))
pyplot.axes([0.1, 0.1, 0.8, 0.8])

labels = '2 fish', '3 fish', '4 fish', '5 fish', '6 fish', '7 fish', '8 fish', '9 fish', '10 fish'
fracs = [3.6, 10.8, 7.8, 10.8, 11.4, 8.4, 9.6, 16.9, 20.5]
explode = (0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11)

pyplot.pie(fracs, explode=explode, labels=labels, colors=('b', 'g', 'r', 'c', 'm', 'y', 'w'), autopct='%1.1f%%', shadow=False)
pyplot.title('Number of fish eaten by Penny on datelist', bbox={'facecolor':'0.85', 'pad':10})

pyplot.savefig(image_file)
dhtml.image(image_file)
