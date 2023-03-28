import random
import linecache
import time
from tweets import handle_tweet

CARTI_SLANG = [":( 💕\n", "🍄", " lit **!++", "+:) love !", "*+!:) !!\n", "\nxo !", "* +", "\n +", "++**", " slatt", ".$", ".. ", "++*", "^\n", "++!", ":)", ":^/", "!", ":-)", "*", "!+", "++", "_"]
CARTI_EMOJIS = ["🦋", "❤️", "🦇", "💕", "💔", "🖤", "🍄"]

def cartify(message):
    words = message.split()
    cartified_message = ""
    for word in words:
        cartified_message += word + " "
        if random.random() < 0.5:
            cartified_message += random.choice(CARTI_SLANG)
        if random.random() < 0.13:
            cartified_message += random.choice(CARTI_EMOJIS) + " "
    return cartified_message

def handle_bars(message):
    args = message.split()
    if len(args) == 1:
        return handle_bars(message + " 2")
    if len(args) > 2 or not args[1].isdigit():
        return "`bars` takes only one int argument!"
    amt = int(args[1])
    if not (1 <= amt <= 8):
        return "can spit out only 1-8 bars!"

    with open("lyrics/lyrics.txt", 'r') as fp:
        lines = fp.readlines()
        output = ""
        lineno = random.randint(0, len(lines) - amt)
        for _ in range(amt):
            output += lines[lineno]
            lineno += 1
        return "*" + output.strip()+ "*"

def update_daily_lyrics():
    global DAILY_LYRICS
    interval = 24 * 60 * 60 # 24 hours
    while True:
        DAILY_LYRICS = daily_lyrics()
        time.sleep(interval)

def daily_lyrics():
    with open("lyrics/lyrics.txt", 'r') as fp:
        lines = fp.readlines()
        output = ""
        lineno = random.randint(0, len(lines) - 2)
        for _ in range(random.randint(1, 3)):
            output += lines[lineno]
            lineno += 1
        return "*" + output.strip() + "*"

def handle_response(message) -> str:
    p_message = message.lower()
    cmd = p_message.split()[0]

    if cmd == "!hello":
        return "*hey my slatt+!" + cartify("\ntoday is daily lyrics are ") + "*\n\n" + DAILY_LYRICS
    elif cmd == "!cartify":
        return cartify(p_message.split(' ', 1)[1])
    elif cmd == "!bars":
        return handle_bars(message)
    elif cmd == "!disaster":
        return "NARCISSIST 09/13/21"
    elif cmd == "!tweet":
        return handle_tweet(message)
    elif cmd == "!peak":
        return "PEAK HAS BEEN LEAKED ON MARCH 23, 2023:\n https://youtu.be/eXAVJcgwNSc"
    elif cmd == "!cartihelp":
        return "I can do:\n`!bars <amount of lines>`,\n`!cartify <message>`,\n`!tweet`,\n`!disaster`,\n`!peak`,\n`!hello`, \n`!daily` for now.\n\nUse `?` for pm."
    elif cmd == "!daily":
        return DAILY_LYRICS
    else:
        return
