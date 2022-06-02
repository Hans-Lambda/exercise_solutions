user = ["A", "B", "C", "D", "E"]
prioritized_users = ["A", "C"]
messengers = ["Whatsapp", "Telegram", "Facebook"]
prioritized_messengers = ["Whatsapp", "Facebook"]

whatsapp = []
telegram = []
facebook = []


message = "important message"

def send_message():
    for u in prioritized_users:
        for m in prioritized_messengers:
            pm = (f"Message for {u}: {message}")
            if m.lower() == "whatsapp":
                whatsapp.append(pm)
            if m.lower() == "telegram":
                telegram.append(pm)
            if m.lower() == "facebook":
                facebook.append(pm)


if __name__ == '__main__':
    send_message()
    print(f"Whatsapp: {whatsapp}")
    print(f"Facebook: {facebook}")

