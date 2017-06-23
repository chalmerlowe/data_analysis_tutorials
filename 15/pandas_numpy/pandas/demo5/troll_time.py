# the twoll timezone appears to only be
# present in version 2014.3 of pytz, which can be found bundled with version 3.4 of python.

import pytz
print('pytz version:', pytz.version)

from datetime import datetime
troll = pytz.timezone('antarctica/Troll')
print('Current Time in Troll Timezone:', datetime.now(tz=troll))