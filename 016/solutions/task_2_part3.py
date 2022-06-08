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


def get_author(author_name):
    for author in users:
        if author['name'] == author_name:
            return author
    return None


def author_average_reads(author_name):
    # we put our code here
    author = get_author(author_name)
    # check if the author is a reviewer

    if author and author.get('type', None) == 'Reviewer':
        # if author and author['type'] == 'Reviewer': # alternative
        return 0

    total = 0
    number_of_published_items = 0
    if author:
        items = author.get('items', [])  ## giving an empty list if not found!!
        for item in items:
            if item["status"] == "Published":
                total += item["reads"]
                number_of_published_items += 1

    return int(total / number_of_published_items) if number_of_published_items > 0 else 0


def author_is_popular(author_name):
    author = get_author(author_name)
    # mindblow approach!!!
    return bool(
        author
        and author['items']
        and (sum(
            [article["reads"] for article in author['items']
             if 'reads' in article and article['status'] == 'Published']) / len(author['items']) > 1000)
    )


def author_is_popular_v2(author_name):
    """
    Find author that is popular i.e. reads greater than 1000
    :param author_name:
    :return: bool
    """
    author = get_author(author_name)
    if author:
        items = author.get('items', [])  # default value of items is now [] if property does not exist
        popular_items = [item['reads'] for item in items
                         if item['status'] == 'Published']
        average_of_popular_items = sum(popular_items) / len(popular_items) if popular_items else 0
        # line above can be written as
        # if popular_items:
        #     average_of_popular_items = sum(popular_items) / len(popular_items)
        # else:
        #     average_of_popular_items = 0
        # You can also write more code as well to make it readable
        return average_of_popular_items > 0  # returns either True or False
    return False


if __name__ == '__main__':

    # To see results, uncomment some of the code blocks below

    # print("Clark", author_average_reads("Clark"))
    # print("Peter", author_average_reads("Peter"))
    # print("Samantha", author_average_reads("Samantha"))
    # print("Mathilda", author_average_reads("Mathilda"))
    # print("Mario", author_average_reads("Mario"))

    # sample code from task 3
    # print("Clark", author_is_popular("Clark"))
    # print("Peter", author_is_popular("Peter"))
    # print("Samantha", author_is_popular("Samantha"))
    # print("Mathilda", author_is_popular("Mathilda"))
    # print("Mario", author_is_popular("Mario"))

    # traditional version
    # print("Clark", author_is_popular_v2("Clark"))
    # print("Peter", author_is_popular_v2("Peter"))
    # print("Samantha", author_is_popular_v2("Samantha"))
    # print("Mathilda", author_is_popular_v2("Mathilda"))
    # print("Mario", author_is_popular_v2("Mario"))
