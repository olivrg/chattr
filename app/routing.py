from channels import route


# display all messages received in the console
def message_handler(message):
    print(message['text'])


channel_routing = [
    route("websocket.receive", message_handler)  # register message hansdler
]
