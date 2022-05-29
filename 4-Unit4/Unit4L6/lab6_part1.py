# ble_scanner.py
# scans for nearby BLE devices and display advertisements

# import BLERadio from module
from adafruit_ble import BLERadio

# create a BLERadio object called ble
ble = BLERadio()

# Let user kow what is going on...
print("scanning for ble")

# use set() function to create two python sets
# python sets are unordered, unindexed, data structures with no duplicate items
found = set()
scan_responses = set()

# start the ble scan and loop over the advertisements found
for advertisement in ble.start_scan():
    addr = advertisement.address
    # if the advertisement has a scan_response and it is not already in the set
    # add it to the scan_responses set
    if advertisement.scan_response and addr not in scan_responses:
        scan_responses.add(addr)
    # if the advertisement has no scan_response and it is not already in the found set
    # add it to the found set
    elif not advertisement.scan_response and addr not in found:
        found.add(addr)
    else:
        continue
    # display the address and advertisement
    print(addr, advertisement)
    print("\t" + repr(advertisement))
    print()


print("scan done")


