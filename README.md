# Udacity_Fsnd_Log_Analysis_Project

**About the Project:**
This project will strech our SQL skills and get practice interacting with aa large database
over a million rows both from the command line and from the code. We will build and refine
complex queries and then use them to draw business conclusions from data. The task is to
create a reporting tool that points out reports (in plain text) based on the data in the
news database. This reporting tool is a Python program using the psycog2 module to connect
to the database.

These are the questions the reporting tools should answer
1.What are the most popular three articles ao all times
2. Who are the most popular article authors at all times
3. On which dyas did more than 1% of requests lead to errors?

**Tools Needed:**
Python3
Vagrant
Virtual Box

**Running the Project:**

**SetUp:**

1.Install Vagrant and Virtual Box
2.Download or clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

**To Run:**

1. Inside the vagrant subdirectory, run the command vagrant up.
2. When vagrant up is finished running, you will get your shell prompt back.
   At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

**Download the data:**

Next, download the data here. You will need to unzip this file after downloading it.
The file inside is called newsdata.sql. Put this file into the vagrant directory,
which is shared with your virtual machine.

**Setting up the database:**

To load the data, use the command psql -d news -f newsdata.sql.

Use psql -d news to connect to database.

The database includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.

**Creating views:**

Create view articlesauthors_v as
select articles.author, count(log.path) as
views from articles,log
where log.path like '%'||articles.slug and
log.status like '%200%'
group by articles.author
order by views desc;

Column |  Type    |
--------+---------+
 author | integer |
 views  | bigint  |


create view b1 as
select to_char(time,'FMMonth FMDD, YYYY') as date, count(status) as total from log
where status = '404 NOT FOUND'
group by to_char(time,'FMMonth FMDD, YYYY');

Column |  Type   |
--------+--------+
 date   | text   |
 total  | bigint |

create view b2 as
select to_char(time,'FMMonth FMDD, YYYY') as date, count(status) as total from log
group by to_char(time,'FMMonth FMDD, YYYY');

 Column |  Type  | Modifiers
--------+--------+-----------
 date   | text   |
 total  | bigint |

create view rate_val as
select b2.date,round(cast(cast(b1.total*100 as float)/cast(b2.total as float) as numeric),2)
as val from b1,b2
where b1.date = b2.date;

Column |  Type   | Modifiers
--------+---------+-----------
 date   | text    |
 val    | numeric |

**Running the queries:**

From the vagrant directory inside vitual machine run news_data.py
$ python3 news_data.py

