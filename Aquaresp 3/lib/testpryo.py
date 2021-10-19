import os
import time
from pyrolib import PyroDevice


firesting = PyroDevice('COM3') # or e.g. COM4, etc on Windows
firesting.channels[2].active = False # deactivate Channel 3
firesting.channels[3].active = False # deactivate Channel 3
firesting.channels[4].active = False # deactivate Channel 4
firesting.channels[1].settings['salinity'] = 35 # in g/L e.g. 35 for seawater

# firesting.channels[2].settings['salinity'] = 0.1
firesting.channels[1].settings['temp'] = 20 # use Pt100-temperature

# firesting.channels[2].settings['temp'] = 37 # use fixed temperature setting
interval = 5
while True:
    start = time.time()
    result = firesting.measure()
    for channel, data in result.items():
        timestamp = data.pop('time')

        fname = 'logfile{}.txt'.format(channel)

    if not os.path.exists(fname): # write header if file does not exist
        with open(fname, 'w') as f:
            f.write('date_time,')
            f.write(','.join(sorted(data)))
            f.write('\n')

    with open(fname, 'a') as f:
        f.write(time.strftime('%Y-%m-%d %H:%M:%S,', time.gmtime(timestamp)))
        f.write(','.join([str(data[k]) for k in sorted(data)]))
        f.write('\n')

    wait_time = start + interval - time.time()
    if wait_time > 0:
        time.sleep(wait_time)
