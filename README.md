## SDSS Computing Studies Python Assignment
### Assignment #xx (Total Marks xx)

Objectives:
* Write a query to search/select data from a table


Once we have a database with information in the tables, the next thing to do is search the database and pull out all relevant information. Sometimes we may want to search for specific items, or order them in a specific way. We may also want to limit the number of results if there are too many.
Often the results will be retrieved as a list or a list of lists.  It will depend on the Python commands we issue it.

Step 1: Build your Query
Structure:
```
select _items_ from _table_ _options_
```
The keyword "select" tells us that we are looking for rows/records in a table.  We can choose which columns we select, or we can use the * to say we want all of the columns for the record.  Note that if we try to select a column that does not exist, our query will have an error.

Consider the table created with the following command:

```
create table if not exists customers (
    id integer primary key autoincrement,
    name tinytext,
    email tinytext,
    cnum int);
```

Some valid searches include the following:
```
select name from customers
select name,cnum from customers
select name from customers where cnum > 10
select name from customers order by name asc
select * from customers order by cnum desc
select * from customers limit 20
select * from customers where (cnum > 5 and (name like '%Be%' or name like '%Da'))
```
Note that in the last 5 commands, there are some options that have been included.
These include:
where : like a conditional statement, only selects records that meet this criteria.  Note that you can use and/or operators and brackets for order of operations
order by *** asc/desc : sorts the records into ascending or descending order by a specific column
limit : sometimes there are a lot of results...Maybe you want to limit them to a smaller set.

Search results are retrieved and stored using the cursor.fetchall() or cursor.fetchone() commands, depending on wehther you want all results or a single record.  See the ex6.getRecords.py and sample.py files for some examples.

Note: 


Assignment:

Answer the following questions about NPC's from the database. They are stored in a table called _npc_

What is the structure of the table?  What are the columns and what datatypes do they store?

How many records are in the table?
How many Knights are in the table?
Which class has the highest number of members?
What is the ID number of the Jester with the most gold?
What is the total gold of the 100 wealthiest npc's in the table?
What is the total gold of the 100 wealthiest npc's under level 5?
What is the stats of the Bard with the highest strength?
What is the ID number of the npc with highest total sum of their 6 primary stats?
What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?
What is the average hitpoints per level of the npc's that are level 10 or higher?

Problem:
Knights, Warriors, Barbarian, Samurai and Rangers have Strength as their Primary Stat
Sages, Sorcerers, Bards and Jesters have Intelligence as their primary stat
Thieves, Assassins and Monks have Dexterity as their primary stat
Pirests have Wisdom as their primary stat

Determine how many NPC's have chosen the wrong class based on their statistics:
example:
NPC 9906 has:
str 5
int 7
wis 10
dex 8
con 6
cha 5
They have picked the correct class because their wisdom stat was the highest


