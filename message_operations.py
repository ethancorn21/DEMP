#builds json formatted message
#needs target, from, timestamp, payload, message type
#message type = message or encryption key
import json

def encapsulated_message(passed_message):
    sender = passed_message.author.id
    timestamp = str(passed_message.created_at)
    # 2 types of messages : 
    # keys and ciphertext (for now plaintext until encryption implemented)
    message_type = "plaintext"
    message_metadata = {
        "type" : message_type,
        "sender" : sender,
        "timestamp": timestamp,
        "payload" : passed_message.content
    }

    finished_message = json.dumps(message_metadata, indent = 4)
    return finished_message

# pass received messages to be decrypted

# 