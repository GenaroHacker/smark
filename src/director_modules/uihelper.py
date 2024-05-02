import sys
import time
import os

class UIHelper:
    SOUNDS_DIR = os.path.join('assets', 'sounds')

    def sleep(self, minutes=0, seconds=0):
        total_seconds = minutes * 60 + seconds
        interval = total_seconds / 40
        for i in range(1, 41):
            time.sleep(interval)
            progress = '#' * i
            remaining = '-' * (40 - i)
            sys.stdout.write('\r[{}]'.format(progress + remaining))
            sys.stdout.flush()
        print()

    def clear(self):
        os.system('clear')