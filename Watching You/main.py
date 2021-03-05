import core.IPinfo as ipinfo
import core.Phoneinfo as phoneinfo

menu = """
 __          __   _       _     _          __     __         
 \ \        / /  | |     | |   (_)         \ \   / /         
  \ \  /\  / /_ _| |_ ___| |__  _ _ __   __ \ \_/ /__  _   _ 
   \ \/  \/ / _` | __/ __| '_ \| | '_ \ / _` \   / _ \| | | |
    \  /\  / (_| | || (__| | | | | | | | (_| || | (_) | |_| |
     \/  \/ \__,_|\__\___|_| |_|_|_| |_|\__, ||_|\___/ \__,_|
                                         __/ |               
                                        |___/        

    [ TelegramChannel: https://t.me/tovidedingrob ]
               [ Telegram: @n1ghtl0ver ]




                <-=[Select function]=->        

    [1] = GetIPInfo - Getting information about the IP-Address
    [2] = GetPhoneInfo - Getting information about the Phone Number
"""
print(menu)

choise = input('[~] Enter select: ')


if choise == '1':
    ipinfo._GetIPInfo()


elif choise == '2':
    phoneinfo._GetPhoneInfo()


else:
    print('\033[31mPermission is not the correct value')