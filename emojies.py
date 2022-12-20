import emoji

emoji_dict = {
    "smiley": chr(128516),
    "sad": chr(128530),
    "wink": chr(128521)
}

message = "yesterday i was feeling " +emoji_dict["smiley"] + " but today" + emoji_dict["sad"] + " it is a terrible day " +emoji_dict["wink"]
print(message)