from nose.tools import *
from counters import *
import pymongo


def db():
    """
    Returns a new mongo connection to a test database, on the default port.
    """
    client = pymongo.MongoClient()
    return client.test_shiny_bear_db


def collection():
    return db().counters


def drop_counters_collection():
    collection().drop()


# ------------------------
# plain functions tests
# ------------------------

def test_set():
    eq_(collection().count(), 0)
    set_counter(collection(), "test")
    eq_(collection().count(), 1)


# ------------------------
# class Counter tests
# ------------------------

@with_setup(drop_counters_collection)
def test_counters_inits_with_0():
    c = Counter(collection(), "test")
    eq_(0, c.counter)


@with_setup(drop_counters_collection)
def test_counters_is_convertable_to_int():
    c = Counter(collection(), "test")
    print c
    eq_(0, int(c))


@with_setup(drop_counters_collection)
def test_counters_is_compareable_to_int():
    c = Counter(collection(), "test")
    print c
    eq_(0, c)
    ok_(-1 < c)
    ok_(1 > c)


@with_setup(drop_counters_collection)
def test_counters_supports_add():
    c = Counter(collection(), "test")
    eq_(c + 1, 1)
    eq_(c + 3, 3)


@with_setup(drop_counters_collection)
def test_counters_supports_sub():
    c = Counter(collection(), "test")
    eq_(c - 1, -1)
    eq_(c - 3, -3)


@with_setup(drop_counters_collection)
def test_counters_supports_iadd():
    c = Counter(collection(), "test")
    eq_(c, 0)
    c += 1
    ok_(type(c) is Counter)
    eq_(c, 1)
    c += 3
    ok_(type(c) is Counter)
    eq_(c, 4)


@with_setup(drop_counters_collection)
def test_counters_supports_isub():
    c = Counter(collection(), "test")
    eq_(c.counter, 0)
    c -= 1
    ok_(type(c) is Counter)
    eq_(c.counter, -1)
    c -= 3
    ok_(type(c) is Counter)
    eq_(c.counter, -4)


@with_setup(drop_counters_collection)
def test_for_each_counter_name_there_shoud_be_only_one_instance():
    c1 = Counter(collection(), "test")
    c2 = Counter(collection(), "test")
    ok_(c1 is c2)


@with_setup(drop_counters_collection)
def test_counters_store_value_in_collection():
    eq_(collection().count(), 0)
    c = Counter(collection(), "test")
    eq_(collection().count(), 1)
    c += 2
    eq_(collection().count(), 1)
    db_value = collection().find_one({'name': "test"})
    eq_(db_value['counter'], 2)


@with_setup(drop_counters_collection)
def test_counters_load_initial_value_from_collection():
    collection().insert(
        {'name': "from_init",
         'counter': 10})
    c = Counter(collection(), 'from_init')
    eq_(c, 10)

# def test_counters_use_type_as_prefix():
#     assert False


# def test_counter_if_no_type_is_given_no_prefix_is_used():
#     assert False
