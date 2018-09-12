# Twitter Network Graphs
Create a directed network of Twitter followers.
Based on https://shkspr.mobi/blog/2015/03/this-is-what-a-graph-of-8000-fake-twitter-accounts-looks-like/

These scripts work in three parts.

1. Taking an initial user, download information about who they follow. Repeat recursively.
2. Generate a directed graph.
3. Draw an image of the graph.

[![Buy me a coffee](https://www.ko-fi.com/img/donate_sm.png)](https://ko-fi.com/edent)


## Usage

### Extract The Information
* Choose the user you wish to track - for example `@edent`.
* Decide what recursive depth you want to go.  A depth of 1 or 2 should be done in a few hours (depending on how many people they are following), a depth of 5 can take several days.

    python GetFollowing.py -s edent -d 2

This will generate a directory structure like
```
.
├── following
│   ├── edent.csv
│   ├── alice.csv
│   ├── bob.csv
│   └── carol.csv
└── twitter-users
    ├── 3104869030.json
    ├── 3105479302.json
    ├── 3111045413.json
    └── 3112012750.json
```

The `following` directory is contains the Twitter Usernames. Each is a `.csv` file showing who they are following.

The `twitter-users` directory contains a `.json` representation of each user.  The file name is their Twitter ID.

### Generate The Network

This script parses the `.csv` files and creates a new `.csv` which contains the Following graph.

    python GenerateNetwork.py -s edent
    
The file `twitter_network.csv` contains a comma delimited graph

```
3112012750,3111045413,1
3111045413,3111252693,2
```

Column 1 is the Twitter ID of a User.  Column 2 is the ID of a User they follow.  Column 3 is the number of followers the User has.

### Draw The Graph

If you want to create a visual representation, you can import `twitter_network.csv` into your favourite stats package.  Or, you can run

    python DrawGraph.py
    
## Credits

Some scripts based on http://mark-kay.net/2014/08/15/network-graph-of-twitter-followers/

With permission granted from the original author to adapt https://twitter.com/markleekay/status/574362042204815361

For more information, please see https://shkspr.mobi/blog/2015/03/this-is-what-a-graph-of-8000-fake-twitter-accounts-looks-like/
