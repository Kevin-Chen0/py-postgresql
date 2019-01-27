# -*- coding: utf-8 -*-

import pandas as pd
import unicodedata


class CreateTable:

    def __init__(self, name):
        COLUMNS = ('name', 'type', 'null', 'unique', 'collate', 'check')
        self.name = name
        self.fields = pd.DataFrame(columns=COLUMNS)  # fields DataFrame
        self.primary_key = None
        self.foriegn_key = None
        self.view = False

    def add_field(self, col_name, data_type, can_null=True, is_unique=False,
                  collate=None, constraint=None):
        field_header = self.fields.columns.tolist()

        can_null = ' NOT NULL' if not can_null else ''
        is_unique = ' UNIQUE' if is_unique else ''

        field_values = [col_name, data_type, can_null, is_unique, collate,
                        constraint]
        new_field = pd.DataFrame(data=dict(zip(field_header, field_values)),
                                 index=[0])
        self.fields = self.fields.append(new_field, ignore_index=True)

    def remove_field(self, name_value):
        self.fields[self.fields.name != name_value]

    def __str__(self):
        string = f"CREATE TABLE {self.name} ("
        for index, row in self.fields.iterrows():
            string += f"{row['name']} {row['type']}{row['null']}"\
                      f" {row['unique']}, "
        string = string[:-2]
        string += ');'
        return string


class InsertTable:

    def __init__(self, name, fields=None):
        self.name = name
        self.fields = pd.DataFrame(columns=fields)

    def add_row(self, *args):
        field_header = self.fields.columns.tolist()
        field_values = [arg for arg in args]
        new_field = pd.DataFrame(data=dict(zip(field_header, field_values)),
                                 index=[0])
        self.fields = self.fields.append(new_field, ignore_index=True)

    def is_num(self, element):
        try:
            float(element)
            return True
        except ValueError:
            pass
        try:
            unicodedata.numeric(element)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def __str__(self):
        string = f"INSERT INTO {self.name} VALUES"
        for index, row in self.fields.iterrows():
            string += " ("
            for item in row.values:
                string += f"{item}, " if self.is_num(item) else f"'{item}', "
            string = string[:-2]
            string += "),"
        string = string[:-1]
        return string
