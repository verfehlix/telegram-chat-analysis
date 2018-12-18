import json
import codecs

# parameters
export_file_path = "data/DataExport_18_12_2018"
results_filename = "results_fff_boys_only.json"

# function that prints all group titles, chronologically
def print_group_titles(messages):
    print("\n################")
    print("# Group Titles #")
    print("################\n")
    for message in messages:
        if message["type"] == "service" and message["action"] == "edit_group_title":
            print(message["date"].split("T")[0], message["title"])

# load file and parse json
with open(export_file_path + "/" + results_filename, encoding='utf-8') as f:
    messages = json.load(f)["messages"]

    # print group titles
    print_group_titles(messages)

    # TODO: message count total and per day / per user

    # TODO: most used words (with stop word removal) in total & per user (maybe sentiment analysis)

    # TODO: most used emojis in total & per user

    # TODO: most used sticker in total & per user

    # TODO: most used domains (in links sent) in total & per user

    # TODO: average sent image in total & per user