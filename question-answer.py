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
cursor.execute("select class, count(*) from npc group by class order by count(*) desc limit 1")
members = cursor.fetchall()
print("Class with highest members:", members)

#ID num of jester with most gold
cursor.execute(" select id from npc where class = 'Jester' order by gold desc limit 1")
jester = cursor.fetchall()
print("ID of Jester with the most gold:", jester)

#total gold of the 100 wealthiest npc's in the table
cursor.execute("select sum(gold) from (select gold from npc order by gold desc limit 100)")
numGold = cursor.fetchall()
print("total gold of 100 wealthiest NPC's in the table is: ", numGold)

#total gold of the 100 wealthiest npc's under level 5
cursor.execute("select sum(gold) from npc where level < 5 order by gold desc limit 100")
numLVL5 = cursor.fetchall() 
print("Total gold of 100 wealthiest NPC's under level 5: ", numLVL5)

#stats of the Bard with the highest strength
cursor.execute("select * from npc where class = 'Bard' order by strength desc limit 1")
fard = cursor.fetchall()
print("stats of the bard with the highest strength: ", fard)

#ID number of the npc with highest total sum of their 6 primary stats
cursor.execute(" select id from npc order by (strength + dexterity + constitution + intelligence + wisdom + charisma) desc limit 1")

primbyaccount = cursor.fetchall()
primbyaccount = round(2, primbyaccount)
print("ID number of the NPC with the highest total sum of their 6 primary stats: ", primbyaccount)

#percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors
cursor.execute("select(select count(*) from npc where class = 'Warrior') * 100.0 /(select count(*) from npc where class in ('Barbarian', 'Warrior', 'Knight', 'Samurai'))")
fightclass = cursor.fetchall()
print("percentage of all fighter classes are warriors: ", fightclass)

#average hitpoints per level of the npc's that are level 10 or higher
cursor.execute("select avg(hp) from npc where level >= 10")
hp = cursor.fetchall()
print("average hitpoints per level of the NPC's that are level 10 or higher: ", hp)

