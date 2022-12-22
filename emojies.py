import emoji

""" emoji_dict = {
    "smiley": chr(128516),
    "sad": chr(128530),
    "wink": chr(128521)
}

message = "yesterday i was feeling " +emoji_dict["smiley"] + " but today" + emoji_dict["sad"] + " it is a terrible day " +emoji_dict["wink"]
print(message) """

msg = input(">" )
words = msg.split(' ')
emojies = {
    'smiley': chr(128516),
    'sad': chr(128530),
    'wink': chr(128521)
}
output = ''
for word in words:
    output+=emojies.get(word, word) + " "
    print(output)
 