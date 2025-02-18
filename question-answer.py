"""
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
"""
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

#structure of table
cursor.execute("pragma table_info(npc_table)")  
columns = cursor.fetchall()
print("Table structure:", columns)

#number of records
query = """select * from npc"""
cursor.execute(query)
result = cursor.fetchall()
record = len(result)  
print("Total number of records:", record)

#number of knights
cursor.execute("select * from npc where class = 'Knight'")  
knight = cursor.fetchall()
knight_count = len(knight)
print("Number of Knights:", knight_count)

#class with highest members
cursor.execute("""
    select class, count(*)
    from npc
    group by class
    order by count(*) desc
    limit 1
""")
members = cursor.fetchall()
print("Class with highest members:", members)

#ID num of jester with most gold
