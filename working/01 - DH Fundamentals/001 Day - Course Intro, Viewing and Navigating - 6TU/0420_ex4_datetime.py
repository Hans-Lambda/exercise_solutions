#import datetime
# import datetime - imports whole package - need to specify, hence datetime.datetime.now()


#def current_date():
    #return datetime.datetime.now()


from datetime import datetime
# from datetime import datetime - import module of package


def current_date2():
    return datetime.now()


if __name__ == '__main__':
    #print(current_date())
    print(current_date2())
