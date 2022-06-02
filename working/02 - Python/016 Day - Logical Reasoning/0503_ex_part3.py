# Task 1:
# We will now use the following list of users in a blog site:
# Define a function named has_hits with one required parameter as a String containing the name of the author we
# want to query.
# The function will return a Boolean (strictly of type Boolean) indicating if that author has any hit article.
# An article is a hit if it has more than 1000 reads.

users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]


def has_hits(author):
    for user in users:
        if author == user["name"]:
            return user["items"] != []


# Task 2:
# Using the same list of users, now define a function named author_average_reads with one required parameter as a String
# containing the name of the author we want to query.
# The function will return an Integer representing the average amount of reads an author has in all its Published
# articles.
# You may use multiple conditionals in if ... elif ... structures.
# You will have to take into account that Reviewers' items do not have a "reads" key. Their average amount should be 0.
# You will also have to take into account Authors with an empty list of items.
# And also make sure the function does not return an error if we type the name of an author that does not exist.
# Remember to base the calculation only on the articles with the status set to Published.


def author_average_reads(author):
    publications = 0
    result = 0
    for user in users:
        if author == user["name"]:
            for item in user["items"]:
                if "reads" in item and item["status"] == "Published":
                    result += item["reads"]
                    publications += 1
    return int(result / publications) if publications > 0 else result


# Task 3:
# Using the same list of users, now define a function named author_is_popular with one required parameter as a String
# containing the name of the author we want to query.
# The function will return a Boolean (strictly a type Boolean) indicating if the average number of reads of all
# Published articles of a particular author is greater than 1000.
# You are NOT allowed to use any if conditionals except when checking for the Published flag.
# You are not allowed to use the author_average_reads function from the previous exercise.


def author_is_popular2(author):
    reads = 0
    condition = lambda x: x["name"] == author
    for item in filter(condition, users):
        for publication in item["items"]:
            if publication["status"] == "Published":
                reads += publication["reads"]
    return reads > 1000


def author_is_popular(author):
    author = get_author(author)
    return bool(
        author
        and author["items"]
        and (sum([article["reads"] for article in author["items"]
                  if "reads" in article and article["status"] == "Published"]) / len(author["items"]) > 1000)
    )


def get_author(author_name):
    for author in users:
        if author["name"] == author_name:
            return author

# evens = [i for i in list if i % 2 == 0]
# odds = [i for i in list if i % 2 == 1]

def odd_even():
    nlist = [*range(25)]
    evens = [{"even_value": i} for i in nlist if i % 2 == 0]
    odds = [{"odd_value": i} for i in nlist if i % 2 != 0]
    print(evens)
    print(odds)

    list = [{"value": 3}, {"value": 4}, {"value": 5}]
    odds2 = [d for i in list for d in i.values() if d % 2 != 0]
    odds3 = [i["value"] for i in list if i["value"] % 2 != 0]
    print(odds2)


if __name__ == '__main__':
    print("\nTask 1 - has hits\n")
    print("Clark", has_hits("Clark"))
    print("Peter", has_hits("Peter"))
    print("Samantha", has_hits("Samantha"))
    print("Mathilda", has_hits("Mathilda"))
    print("Mario", has_hits("Mario"))
    print("\nTask 2 - average reads\n")
    print("Clark", author_average_reads("Clark"))
    print("Peter", author_average_reads("Peter"))
    print("Samantha", author_average_reads("Samantha"))
    print("Mathilda", author_average_reads("Mathilda"))
    print("Mario", author_average_reads("Mario"))
    print("\nTask 3 - is popular\n")
    print("Clark", author_is_popular("Clark"))
    print("Peter", author_is_popular("Peter"))
    print("Samantha", author_is_popular("Samantha"))
    print("Mathilda", author_is_popular("Mathilda"))
    print("Mario", author_is_popular("Mario"))

    odd_even()
