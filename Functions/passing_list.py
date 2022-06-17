# usernames = ['hannah', 'ty', 'margot']
#
# def print_usernames(usernames):
#     for username in usernames:
#         print(username)
#
# print_usernames(usernames)

messages = ["hello there", "how are u?", ":)"]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
    # return messages, sent_messages
send_messages(messages[:], sent_messages)
show_messages(messages)
show_messages(sent_messages)

#wsdsddssd
