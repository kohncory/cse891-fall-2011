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
            fish = fish_list[i]
            date_list = dates_d.get(fish, [])
            date_list.append(date)
            temp = set(date_list)
            date_list = list(temp)
            date_list.sort()
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
    global fishfromdatelist
    fishfromdatelist = []
    datelistdict = {}
    for date in datelist:
        datelistdict[date] = get_fishes_by_date(fish_d, date)
        for item in datelistdict.values():
            fishfromdatelist.extend(item)
    return fishfromdatelist


def get_dates_by_fishlist(some_d, fishlist):
    global datesfromfishlist
    datesfromfishlist = []
    fishlistdict = {}
    for fish in fishlist:
        try:
            if not some_d[fish]:
                pass
        except:
            some_d = dates_d
        fishlistdict[fish] = get_dates_by_fish(some_d, fish)
        for item in fishlistdict.values():
            datesfromfishlist.extend(item)
    return datesfromfishlist
        


fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
dates_d = make_dates_dict(fish_d)


###

# test 1
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x

###

# test 2
x = get_dates_by_fish(dates_d, 'salmon')
#print x
assert '1/1' in x
assert '1/2' in x

###

# test 3
x = get_fishes_by_datelist(fish_d, ['1/1'])
assert 'salmon' in x, x

###

# test 4
x = get_dates_by_fishlist(fish_d, ['salmon'])
assert '1/1' in x, x
