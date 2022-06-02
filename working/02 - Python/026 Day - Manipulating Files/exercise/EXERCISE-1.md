<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [My Loved Users](#my-loved-users)
- [World Data - I Know everything](#world-data---i-know-everything)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# My Loved Users


Create a program that reads and loads the `user.json` file as a dictionary in your program. Create the following 
functions:

1. `get_subscribers` returns all the users that are subscribers.
2. `get_active_users` return all active users
3. `get_week_passwords` list all users with week passwords (a strong password must contain both letter and numbers)
4. `get_number_of_users` returns the number of users in the system
5. `login` asks for the user and password and prints on the screen if the login was successful.
    - Login will also fail if the user is inactive.
    - Login will show a message inviting the user to subscribe if he/she is not yet a subscriber.
6. `generate_contact_list` creates a list of users with names and e-mail, e.g.
    - ```
      User One <user@one.email>
      Someone Johnson <someone@email.fake>
      John Doe <john@doe.xyz>
      ```
      
# World Data - I Know everything

Access the Website [Data.World](https://data.world/) (you need to register) or 
[Our World in Data](https://ourworldindata.org). There you will find hundreds of datasets,
as `json` files, choose one that you find interesting. Create a program to load it as a dictionary. Discuss with your
colleague what kind of relevant or interesting data can you extract from the dataset, and try to process it, e.g. calculate
the average, mins and maxs, most frequent values, etc. Create a menu, so that the user can choose which kind of 
information it wants to extract.

- One dataset you can use is the (Data on Energy by Our Workd in Data), here is the [json file](https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.json)