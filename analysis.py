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

# function that prints the message count in total
def print_message_count_total(messages):
    print("\n#######################")
    print("# Total Message Count #")
    print("#######################\n")
    messages = [message for message in messages if message["type"] == "message"]

    print(len(messages))

# load file and parse json
with open(export_file_path + "/" + results_filename, encoding='utf-8') as f:
    messages = json.load(f)["messages"]

    # print group titles
    print_group_titles(messages)

    # TODO: message count total and per day / per user
    print_message_count_total(messages)

    # TODO: most used words (with stop word removal) in total & per user (maybe sentiment analysis)

    # TODO: most used emojis in total & per user

    # TODO: most used sticker in total & per user

    # TODO: most used domains (in links sent) in total & per user

    # TODO: average sent image in total & per user