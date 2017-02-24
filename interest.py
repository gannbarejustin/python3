def interest(money, year, itst):
    global times
    print('{0:5} year = {1:20.5f}'.format(times, money) )
    times += 1
    tot = 0
    if( year == 0):
        return money
    else:
        tot += money * (1 + itst)
        year -= 1
        return interest( tot, year, itst)
      
times = 0
interest(1000000, 20, 0.1)
