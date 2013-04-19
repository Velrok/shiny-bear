#!/usr/bin/env python
# -*- coding: utf-8 -*-
# requires
# - mongodb
# - pymongo
# import pymongo


def __query(name):
    return {'name': name}


def inc_counter(collection, name):
    pass


def set_counter(collection, name, value):
    if collection.find(__query(name)).count() == 0:
        # its a new counter
        collection.insert(
            {'name': name,
             'counter': 0})
    else:
        # its already present -> update
        collection.update(
            __query(name),
            {"$set": {'counter': value}})


def get_counter(collection, name):
    pass


class Counter(object):
    """A mongo db backed counter.

    A counter identity is defined by its name.
        Counter(db, 'counter1') is Counter(db, 'counter1') -> True

    Counters support +, -, +=, -= and can be converted and compared to int.
        Counter(db, "new_counter") == 0 -> True
        Counter(db, "new_counter") == 1 -> False

    Normally Counters are increased and descreaded by a specific amount.
    However if you need to set a value you can do so:
        Counter(db, "new_counter").counter = 10
    """
    instances = {}

    def __new__(cls, collection, name):
        """Ensures identity based on names."""
        if not name in cls.instances:
            cls.instances[name] = object.__new__(cls, collection, name)
        return cls.instances[name]

    def __init__(self, collection, name):
        super(Counter, self).__init__()
        self.collection = collection
        self.name = name

        found = self.collection.find_one(self.__query())
        if found:
            # since we loaded from db there is no need to write it again
            super(Counter, self).__setattr__('counter', found['counter'])
        else:
            self.counter = 0  # write to db

    def __int__(self):
        return self.counter

    def __cmp__(self, other):
        if self.counter < int(other):
            return -1
        elif self.counter == int(other):
            return 0
        else:
            return 1

    def __add__(self, other):
        return self.counter + int(other)

    def __sub__(self, other):
        return self.counter - int(other)

    def __iadd__(self, other):
        self.counter += int(other)
        return self

    def __isub__(self, other):
        self.counter -= int(other)
        return self

    def __query(self):
        return __query(self.name)

    def __store_new_counter_value(self, value):
        if self.collection.find(self.__query()).count() == 0:
            # its a new counter
            self.collection.insert(
                {'name': self.name,
                 'counter': self.counter})
        else:
            # its already present -> update
            self.collection.update(
                self.__query(),
                {"$set": {'counter': value}})

    def __setattr__(self, attr, value):
        super(Counter, self).__setattr__(attr, value)
        if attr == "counter":
            self.__store_new_counter_value(value)

    def __str__(self):
        return "<Counter '{name}':{count}>".format(name=self.name,
                                                count=self.counter)

    def __repr__(self):
        return "<counters.Counter {{'name': '{name}', 'counter': {count}}}>".format(
            name=self.name,
            count=self.counter)
