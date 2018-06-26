from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from database import Base, Information
# from hello import nested_dict

engine = create_engine('sqlite:///crawler1.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
stmt = select([Information])
connection=engine.connect()
# Print the emitted statement to see the SQL emitted
print(stmt)
result = stmt.execute()
my_list=[]
i=0
for row in result:
    i+=1
    print row
    my_list.append(row)
    print "+_+_+_++_+__+_+__+_+_+_++_+_+_++_+_+__+_+_+_+_+_+_+_+_+_"
# Execute the statement and print the results
# print(connection.execute(stmt).fetchall())
# print session.query(Information).all()
# print conn.execute(select([information]))

# Insert a Person in the person table
# new_person = Information(id=1, title='vishal', description='works in shine', date='18 jun', location='gurugram')
# session.add(new_person)
# session.commit()
# i = 0
# for p_id, p_info in nested_dict.iteritems():
#     print("\nPerson ID:", p_id)
#     i += 1
#
#     # for key in p_info:
#     # print(key + ':', p_info[key])
#     new_person = Information(id=i, title=p_info['title'], description=p_info['description'], date=p_info['date'],
#                                  location=p_info['location'])
#     session.add(new_person)
#     session.commit()
# Insert an Address in the address table
# new_address = Address(post_code='00000', person=new_person)
# session.add(new_address)
# session.commit(
