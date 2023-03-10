import random
import linecache
from tweets import handle_tweet

CARTI_SLANG = [":( 💕\n", "🍄", " lit **!++", "+:) love !", "*+!:) !!\n", "\nxo !", "* +", "\n +", "++**", " slatt", ".$", ".. ", "++*", "^\n", "++!", ":)", ":^/", "!", ":-)", "*", "!+", "++", "_"]
CARTI_EMOJIS = ["🦋", "❤️", "🦇", "💕", "💔", "🖤", "🍄" ]

def cartify(message):
    words = message.split()
    cartified_message = ""
    for word in words:
        cartified_message += word
        cartified_message += " "
        if random.randint(0, 1) < 1:  
            cartified_message += random.choice(CARTI_SLANG)
        if random.randint(0, 100) < 13:
                cartified_message += random.choice(CARTI_EMOJIS)
                cartified_message += " "
    return cartified_message

def handle_bars(message):
    if (len(message.split()) != 2):
        return ">>> `bars` takes only one int argument!"
    if not message.split(' ', 1)[1].isdigit():
        return ">>> `bars` arg has to be an int!"
    amt = int(message.split(' ', 1)[1]);
    print(amt)
    if (int(amt) > 8) or (int(amt) < 1):
        return ">>> can spit out only 1-8 bars!"
    with open("lyrics/lyrics.txt", 'r') as fp:
        x = len(fp.readlines())
        output = ""
        lineno = random.randint(1, x)
        while amt > 0:
            added_line = linecache.getline("lyrics/lyrics.txt", lineno, module_globals=None)
            # in case if string is empty, restart algo
            if len(added_line.strip()) == 0:
                print("PROC!")
                return handle_bars(message)
            output += added_line
            amt -= 1
            lineno += 1
        return (">>> " + output)
    
# test
# print(handle_bars("!bars 2"))


    
            
def handle_response(message) -> str:
    p_message = message.lower()
    cmd = p_message.split()[0]

    if p_message == "!hello":
        return ">>> " + "hey my slatt+!"

    elif cmd == "!cartify":
        return ">>> " + cartify(p_message.split(' ', 1)[1])
    
    elif cmd == "!bars":
        return handle_bars(message)
    
    elif cmd == "!disaster":
        return ">>> " + "NARCISSIST 09/13/21"

    elif cmd == "!tweet":
        return ">>> " + handle_tweet(message)

    elif p_message == '!help':
        return ">>> i only can do `!bars <amount of lines>` or `!cartify <message>` for now."
    
    else: 
        return
