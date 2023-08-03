import pyodbc

connection = 'driver=MySQL ODBC 5.3 Unicode Driver;server=127.0.0.1;database=PythonDataB;uid=root;password='''

def select_data():
    with pyodbc.connect(connection) as con:
        sql_select = ''' select * from members '''
        cue = con.cursor()
        cue.execute(sql_select)
        for rows in cue.fetchall():
            print(rows)

def insert_data(cid,cname,clname,cage):
    with pyodbc.connect(connection) as con:
        sql_insert = (''' insert into members(customer_id,customer_name,customer_lastname,customer_age) values ('%s','%s','%s','%s') ''')
        con.execute(sql_insert %(cid,cname,clname,cage))
        
def update_data(uName,uLname,uAge,uId):
    with pyodbc.connect(connection) as con:
        sql_update = ''' update members set customer_name = '%s',customer_lastname = '%s',customer_age = '%s' where customer_id = '%s' '''
        con.execute(sql_update %(uName,uLname,uAge,uId))
        
def delete_data(delid):
    with pyodbc.connect(connection) as con:
        sql_delete = ''' delete from members where customer_id = '%s' '''
        con.execute(sql_delete %(delid))        
        
        
select_data()        
customer_id = input('id: ')
customer_name = input('name: ')
customer_lname = input('lname: ')
customer_age = input('age: ')
insert_data(customer_id,customer_name,customer_lname,customer_age)

select_data() 

update_name = input('name: ')
update_lname = input('lname: ')
update_age = input('age: ')
update_id = input('id: ')

update_data(update_name,update_lname,update_age,update_id)

delete_id = input('Del Id: ')

delete_data(delete_id)

select_data()
