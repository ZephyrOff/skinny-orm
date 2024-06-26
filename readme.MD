# Skinny ORM

"Skinny ORM" - a lightweight Python package that simplifies data storage, manipulation, and retrieval from a SQLite (maybe others later) database using Python dataclasses.


It's not really a "Relational Mapper". It's just a simple way to persist data.

Installation:
- 
```shell script
  pip install skinny_orm
```
or
```shell script
  poetry add skinny_orm
```

Example:
-
- Create your model:
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    name: str
    age: int
    birth: datetime
    percentage: float

```

When defining the model, it is possible to declare an auto-increment variable with the following method
(Auto-increments must be declared at the end of the model because they are optional)
```python
from dataclasses import dataclass
from datetime import datetime
from skinny_orm.sqlite_orm import auto_increment
from typing import Optional

@dataclass
class User:
    name: str
    age: int
    birth: datetime
    percentage: float
    id: Optional[auto_increment] = None

```

- Create a connection et an "orm" object

```python
import sqlite3
from skinny_orm.orm import Orm

connection = sqlite3.connect('database.db')
orm = Orm(connection)
```

- Or only an "orm" object with the name of database
```python
from skinny_orm.orm import Orm

orm = Orm('database.db')
```
connection_type option is available to specify the connector. (Default sqlite3 since it is the only one currently implemented)

You can also use the with method
```python
from skinny_orm.orm import Orm

with Orm('database.db') as orm:
    orm.bulk_insert(users)
```


- And Voila (no need to create tables. if they don't exist, it will create them automatically)

```python
users = [
    User(id=1, name='Naruto', age=15, birth=datetime.now(), percentage=9.99),
    User(id=2, name='Sasuke', age=15, birth=datetime.now(), percentage=9.89),
    User(id=3, name='Sakura', age=15, birth=datetime.now(), percentage=9.79),
]
# Bulk insertions (if the table "User" does not exist, it will create it)
orm.bulk_insert(users)
# Selections (always end with .first() or .all() )
naruto: User = orm.select(User).where(User.name == 'Naruto').first()
the_boys: list[User] = orm.select(User).where((User.name == 'Naruto') | (User.name == 'Sasuke')).all()

# Update data by setting specific fields
orm.update(User).set(User.age == 30).where(User.id == 1)
# Or you can simply update the object with all the fields
naruto.age = 30
orm.update(naruto).using(User.id)

# Bulk update objects
users_20_year_later = [
    User(id=1, name='Naruto', age=35, birth=datetime.now(), percentage=9.99),
    User(id=2, name='Sasuke', age=35, birth=datetime.now(), percentage=9.89),
    User(id=3, name='Sakura', age=35, birth=datetime.now(), percentage=9.79),
]
orm.bulk_update(users_20_year_later).using(User.id)
```
