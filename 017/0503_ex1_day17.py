
# Task 1

roles = {
    "ST": "Student",
    "REST": "Registered student",
    "AL": "Alumni",
    "AN": "Anonymous",
    "TE": "Teacher",
    "AD": "Admin"
}

users = [
    {
        "name": "Holly",
        "role": roles["ST"]
    },
    {
        "name": "Peter",
        "role": roles["ST"]
    },
    {
        "name": "Luke",
        "role": roles["ST"]
    },
    {
        "name": "Janis",
        "role": roles["TE"]
    },
    {
        "name": "Aretha",
        "role": roles["TE"]
    },
    {
        "name": "Ringo",
        "role": roles["AD"]
    }
]

modules = [
    {
        "title": "Computer basics",
        "teacher": "Janis",
        "registered": ["Peter"],
        "alumni": ["Luke", "Holly"]
    },
    {
        "title": "Python basics",
        "teacher": "Janis",
        "registered": ["Holly"],
        "alumni": [],
        "requirement": "Computer basics"
    },
    {
        "title": "Django basics",
        "teacher": "Aretha",
        "registered": [],
        "alumni": [],
        "requirement": "Python basics"
    }
]

module_permissions = {
    roles["AN"]: ["describe"],
    roles["ST"]: ["describe"],
    roles["REST"]: ["describe", "read", "comment"],
    roles["AL"]: ["describe", "read"],
    roles["TE"]: ["describe", "read"],
    roles["AD"]: ["describe", "read", "write", "comment"]
}

def user_role(user_name):
    for user in users:
        if user_name == user["name"]:
            return user["role"]
    else:
        return roles["AN"]


def role_change(user_name, module_name):
    # this replaces just a for loop // for item in modules: if item["title"] == module_name
    condition = lambda x: x["title"] == module_name
    for item in filter(condition, modules):
    # could also be
        if user_name in item["registered"]:
            return roles["REST"]
        if user_name in item["alumni"]:
            return roles["AL"]
        if user_name == item["teacher"]:
            return roles["AD"]


def permissions(role):
    return module_permissions.get(role)


def has_permission(user_name, module_name, permission):
    role = role_change(user_name, module_name) or user_role(user_name)
    return permission in module_permissions[role]


if __name__ == '__main__':

    for permission in module_permissions["Admin"]:
        for module in modules:
            print(f"Can {permission.upper()} on {module['title'].upper()}?")
            print("Anonymous",
                  has_permission("Somebody", module["title"], permission))
            for user in users:
                print(user["name"],
                      has_permission(user["name"], module["title"], permission))
