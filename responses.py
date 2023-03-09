import random

CARTI_SLANG = [":( 💕\n", "🍄", " lit **!++", "+:) love !", "*+!:) !!\n", "\nxo !", "* +", "\n +", "++**", " slatt", ".$", ".. ", "++*", "^\n", "++!", ":)", ":^/", "!", ":-)", "*", "!+", "++", "_"]
CARTI_EMOJIS = ["🦋", "❤️", "🦇", "💕", "💔", "🖤", "🍄" ]


def cartify(message):
    words = message.split()

    cartified_message = ""
    for word in words:
        cartified_message += word
        cartified_message += random.choice(CARTI_SLANG)
        cartified_message += " "
        if random.randint(0, 100) < 13:
            cartified_message += random.choice(CARTI_EMOJIS)
            cartified_message += " "

    return cartified_message


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "!hello":
        return "hey my slatt+!"

    if p_message.split()[0] == "!cartify":
        return str(cartify(p_message.split(' ', 1)[1]))

    if p_message == '!help':
        return "`this is a help message`"
