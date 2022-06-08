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
# Instructions
# The anonymous user is not actually a user, so you may have to write a logical expression to catch this particular
# case.
# The students who are registered (or alumni) in a module will actually need to be checked for permissions
# taking the REST or AL roles instead of ST. You may have to write another logical expression to catch these
# particular cases.
# Teachers have read access to every module, but they should also have Admin access (describe,
# read, write, comment) to the module they are teaching. We do not have a specific role for this case, use the AD
# permissions instead. Again, you may have to add another logical expression to catch this particular case.


def get_user(user_name):
    for user in users:
        if user['name'] == user_name:
            return user
    return None


def get_module(module_name):
    for module in modules:
        if module["title"] == module_name:
            return module
    return None  # here was the problem


def get_module_role(user_name, module_name):
    user = get_user(user_name)
    module = get_module(module_name)
    # return module["registered"]
    if not user:
        mod_role = roles["AN"]
    else:
        if user["role"] == roles["TE"]:
            if module["teacher"] == user_name:
                mod_role = roles["AD"]
            else:
                mod_role = user["role"]
        elif user["role"] == roles["ST"] and module["registered"] and user_name in module["registered"]:
            mod_role = roles["REST"]
        elif user["role"] == roles["ST"] and module["registered"] and  user_name in module["alumni"]:
            mod_role = roles["AL"]
        else:
            mod_role = user["role"]
    return mod_role


def get_permission(user_name, module_name):
    mod_role = get_module_role(user_name, module_name)
    user_permission = module_permissions[mod_role]
    return user_permission


def has_permission(user_name, module_name, permission):
    return permission in get_permission(user_name, module_name)


if __name__ == '__main__':
    for permission in module_permissions["Admin"]:
        for module in modules:
            print(f"Can {permission.upper()} on {module['title'].upper()}?")
            print("Anonymous",
                  has_permission("Somebody", module["title"], permission))
            for user in users:
                print(user["name"],
                      has_permission(user["name"], module["title"], permission))
