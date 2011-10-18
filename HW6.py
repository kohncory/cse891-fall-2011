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
    for date in datelist:
        print date, get_fishes_by_date(fish_d, date)


def get_dates_by_fishlist(dates_d, fishlist):
    for fish in fishlist:
        print fish, get_dates_by_fish(dates_d, fish)
        


fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
dates_d = make_dates_dict(fish_d)

print 'fishlist:', get_fishes_by_date(fish_d, '1/2')
get_dates_by_fishlist(dates_d, fishlist)

print 'dateslist:', get_dates_by_fish(dates_d, 'plaice')
get_fishes_by_datelist(fish_d, datelist)
