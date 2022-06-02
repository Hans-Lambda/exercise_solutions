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


def get_user(user_name):
    # for user in users:
    #     if user['name'] == user_name:
    #         return user
    # return
    """
    Return the first user with a given name
    """
    return next((user for user in users if user["name"] == user_name), None)


def get_module(module_name):
    """
    Return the first module with the given name.
    :param module_name:
    :return:
    """
    return next((module for module in modules if module["title"] == module_name), None)


def is_anonymous(user):
    return not user  # not None -> True -- not "Truthy" false


def has_role_permission(permission, role):
    """
    Return true if a role has default permission access to modules
    """
    return permission in module_permissions[role]


def is_registered(user, module):
    return user and module and user["name"] in module["registered"]


def is_alumni(user, module):
    return module and user['name'] in module["alumni"]


def is_teacher_of(user, module):
    return user and module and user['name'] == module['teacher']


def has_permission(user_name, module_name, permission):
    user = get_user(user_name)
    module = get_module(module_name)
    return (
            is_anonymous(user) and has_role_permission(permission, 'Anonymous')
            or not is_anonymous(user) and (
                # general rule for all roles
                    has_role_permission(permission, user["role"])
                    # catch the registered users
                    or is_registered(user, module) and has_role_permission(permission, roles["REST"])
                    # catch the Alumni
                    or is_alumni(user, module) and has_role_permission(permission, roles["AL"])
                    # Catch the Teacher of the module
                    or is_teacher_of(user, module) and has_role_permission(permission, roles["AD"])
            )
    )


if __name__ == '__main__':
    for permission in module_permissions["Admin"]:
        for module in modules:
            print(f"Can {permission.upper()} on {module['title'].upper()}?")
            print("Anonymous",
                  has_permission("Somebody", module["title"], permission))
            for user in users:
                print(user["name"],
                      has_permission(user["name"], module["title"], permission))
