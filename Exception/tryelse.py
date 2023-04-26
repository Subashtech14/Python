try:
    print("This is windows")
except:
    assert('Linux' in sys.platform),"This runs only on Linux"
else:
    print("Running else")

import sys
try:
    assert('Linux' in sys.platform),"This runs only on Linux"
except:
    print("This is windows")
finally:
    print("Finally")