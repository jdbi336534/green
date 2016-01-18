import sys
import datetime
import os


def modify():
    file = open('zero.md', 'r')
    flag = int(file.readline()) == 0
    file.close()
    file = open('zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m test_github_streak')


def next_day():
    os.system('date -s 20150202')


# from http://stackoverflow.com/questions/12081310/python-module-to-change-system-date-and-time
def linux_set_time(year, month, day, hour, min, sec, mm):
    time_tuple = (year, month, day, hour, min, sec, mm)
    import ctypes
    import ctypes.util
    import time

    # /usr/include/linux/time.h:
    #
    # define CLOCK_REALTIME                     0
    CLOCK_REALTIME = 0

    # /usr/include/time.h
    #
    # struct timespec
    #  {
    #    __time_t tv_sec;            /* Seconds.  */
    #    long int tv_nsec;           /* Nanoseconds.  */
    #  };
    class timespec(ctypes.Structure):
        _fields_ = [("tv_sec", ctypes.c_long),
                    ("tv_nsec", ctypes.c_long)]

    librt = ctypes.CDLL(ctypes.util.find_library("rt"))

    ts = timespec()
    ts.tv_sec = int(time.mktime(datetime.datetime(*time_tuple[:6]).timetuple()))
    ts.tv_nsec = time_tuple[6] * 1000000  # Millisecond to nanosecond

    # http://linux.die.net/man/3/clock_settime
    librt.clock_settime(CLOCK_REALTIME, ctypes.byref(ts))


if __name__ == '__main__':
    os.system('date -s 20160119')
    commit()
