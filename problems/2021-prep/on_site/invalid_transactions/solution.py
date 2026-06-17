def invalid_transactions(transactions):
    mp = {}
    invalid = []
    # we build a map of the data based on time
    for transaction in transactions:
        name, time, amt, city = transaction.split(',')
        time = int(time)

        if time not in mp:
            mp[time] = {name: [city]}
        else:
            if name not in mp[time]:
                mp[time][name] = [city]
            else:
                mp[time][name].append(city)

    for transaction in transactions:
        name, time, amt, city = transaction.split(',')

        if int(amt) > 1000:
            invalid.append(transaction)
            continue

        for time_t in range(int(time) - 60, int(time) + 61):
            if time_t not in mp:
                continue

            if name not in mp[time_t]:
                continue

            if len(mp[time_t][name]) > 1 or mp[time_t][name][0] != city:
                invalid.append(transaction)

    return invalid


if __name__ == '__main__':
    transacts = ["alice,20,800,mtv", "alice,50,100,beijing"]
    tscts2 = ["alice,20,800,mtv", "alice,50,1200,mtv"]
    tscts3 = ["alice,20,800,mtv", "bob,50,1200,mtv"]
    tscts4 = ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"]
    print(invalid_transactions(tscts4))
