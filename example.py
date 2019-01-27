# coding=utf-8

from py_post.sql import Session
from py_post.table import CreateTable, InsertTable


new_table = CreateTable(name='vendor')
new_table.add_field('part_id', 'INT', can_null=False, is_unique=True)
new_table.add_field('part_name', 'VARCHAR(255)')

# Remeber the set your own username and password here.
session = Session(db='test', usr='postgres', pwd='pass')
session.to_sql(str(new_table))

'''
    str(table):
    CREATE TABLE vendor (part_id INT NOT NULL UNIQUE, part_name VARCHAR(255));
'''

field_names = list(new_table.fields['name'].values)
insert_table = InsertTable(name='vendor', fields=field_names)
insert_table.add_row('11111', 'pencil')
insert_table.add_row('22222', 'pen')
insert_table.add_row('33333', 'paper')
insert_table.add_row('44444', 'parcel')
insert_table.add_row('55555', 'package')
session.to_sql(str(insert_table))

'''
    str(table):
    INSERT INTO vendor VALUES (11111, 'pencil'), (22222, 'pen'),
                (33333, 'paper'), (44444, 'parcel'), (55555, 'package')
'''
