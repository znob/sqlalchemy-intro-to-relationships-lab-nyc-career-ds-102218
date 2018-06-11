
# SQLAlchemy One to Many Lab

## Objectives

1.  Create a "has many"/"belongs to" relationship with SQLAlchemy
2.  Add data to a database containing a "has many"/"belongs to" relationship
3.  Query from a database containing a "has many"/"belongs to" relationship

## Actors and Roles

In this lab, we will use SQLAlchemy to programmatically recreate the relationship that existing between actors and all of their roles.  All actors have many roles throughout their careers.  Likewise, each instance of an `Actor` class will have many instances of the `Role` class.

We first will create the database and the models and then populate the tables with a couple well-known actors and roles.  Finally, we will practice querying from the relational database to see which actors have which roles.

### Create the schema

We will write the code for our two model classes in `models.py`.  Alternatively, we could write both models in `models.py` then write Alembic migrations to establish the association between the two models.

**`Role`**

Every `Role` will have an `id` serving as the primary key and a `character` column containing the name for every role.  

To set up the "belongs to" relationship, we will need to add a column called `actor_id` that will use the `ForeignKey()` function to tell SQLAlchemy that this column can contain only values found in the `actors.id` column of the `actors` table.

We also need to use the `relationship` function to tell the ORM that our `Role` class should be associated with the `Actor` class.

In this case, our `relationship` function will accept `'Actor'` as an argument, and its `back_populates` parameter will point back to the `'roles'` table.  The aforementioned `relationship` function should be set to an `actor` variable.  Doing so, lets us obtain the proper Actor instance when we query `Role.actor`.

**`Actor`**

Every `Actor` will have an `id` for its primary key and a `name` column.

We also will need to establish the "one to many" relationship by setting a `roles` variable to a `relationship` function that produces a list of all Role instances associated with that particular Actor instance.  In this case, `relationship` will accept `'Role'` as an argument.  It will `order_by` the resulting list by `Role.id` and its `back_populates` parameter will refer back to an `'actor'`.

### Populate the database

Once you have built the Actor and Role classes and their association, run the `models.py` file to create the database.  Now we can go to the `seeds.py` file to fill in the tables with some actors and roles!

Create the following actors:
* Tom Hanks
* Gwyneth Paltrow
* an actor of your choice

Associate the actors to the following roles.  There should be eight roles in total.
* Tom Hanks
    * Forrest Gump
    * Jim Lovell
    * Woody
    * Robert Langdon
* Gwyneth Paltrow
    * Pepper Potts
    * Margot Tenenbaum
* Your actor
    * a role of your choice
    * a role of your choice    

Remember we can create instances of the Role class while making the association in the following manner:

```python
woody_harrelson = Actor(name='Woody Harrelson')
woody_harrelson.roles = [Role(character='Detective Marty Hart'), Role(character='Mickey Knox')]
```

### Query the related data

In `queries.py` write the following queries:

* `return_gwyneth_paltrows_roles` should return the list of Gwyneth Paltrow's Role instances
* `test_return_tom_hanks_2nd_role` should return the Tom Hanks' second Role instance
