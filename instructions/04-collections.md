## Collections

Python exposes several built-in collection types
that can be used with a clean and easy syntax.

In this section we'll introduce these collections
as well as the comprehension syntax for
easily populating them.

## Lists

Lists are an ordered mutable collection of elements.
They can be created with the [] syntax,
passing in comma separated values.

List elements can be of any type,
but its good practice to have all elements
have the same type.

``` python
groceries = ["bread", "eggs", "milk", "marmite"] # groceries is a list of strings
```

You can get a single element out of a list
by passing its index in '[]'

*NOTE:* Indices in Python are zero indexed

```
>>> groceries[0]
'bread'
>>> groceries[2]
'milk'
>>> groceries[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

You can loop through all elements of a list
using the `for x in y` syntax.

```
>>> groceries = ["bread", "eggs", "milk", "marmite"]
>>> for grocery in groceries:
...     print(grocery)
...
bread
eggs
milk
marmite
```

You can count the number of elements in a list
using the built-in `len()` function.

```
>>> len(groceries)
4
```

You can add an element to a list
by using the list type's `append()`
function

```
>>> groceries.append("cheese")
>>> print(groceries)
['bread', 'eggs', 'milk', 'marmite', 'cheese']
```

and you can add elements from another list
using the list type's `extend()` function.

```
>>> groceries.extend(["tomato sauce", "pears"])
>>> groceries
['bread', 'eggs', 'milk', 'marmite', 'cheese', 'tomato sauce', 'pears']
```

Finally, you can test that an element is in a list
using the `in` keyword.

```
>>> "milk" in groceries
True
>>> "coconuts" in groceries
False
```

## Sets

Sets are collections of unique elements.
They are created using the {} syntax,
but empty sets must be created using `set()`.

```
>>> bool_values = {True, False}
>>> bool_values
{False, True}
```

You can add elements to a set
using the set type's add() method,
but if the element is already present
the set will not be changed.

```
>>> bool_values.add(None)
>>> bool_values.add(True)
>>> bool_values
{False, True, None}
```

You can create a set
from another collection e.g. a list
by passing that collection into the `set()` function.
Note that any duplicate elements will be removed.

```
>>> set(groceries)
{'bread', 'cheese', 'pears', 'eggs', 'marmite', 'milk', 'tomato sauce'}
```

### Exercise - unique characters

Write a function that returns
the number of unique characters
in a given string.

Hint: Passing a string into `set()`
      will create a set from its characters.

The output should be something like this:
```
>>> count_unique_characters("cake")
4
>>> count_unique_characters("Hello")
4
```

## Dictionaries

Dictionaries map unique keys to values.
They are also created using the `{}` syntax
and can be queried by passing a key
into square brackets
(in a similar way to how lists are queried by index).

```
>>> asil = {"name": "Asil", "employer": "Microsoft", "height (cm)": 168}
>>> asil["name"]
'Asil'
```

You can also add items to a dictionary using the `[]` syntax.

```
>>> asil["pronouns"] = "he/him"
>>> asil
{'name': 'Asil', 'employer': 'Microsoft', 'height (cm)': 168, 'pronouns': 'he/him'}
```

Its possible to nest lists into dictionaries as values.

```
>>> asil["cats"] = ["Fluffy", "Sheru Khan"]
>>> asil
{'name': 'Asil', 'employer': 'Microsoft', 'height (cm)': 168, 'pronouns': 'he/him', 'cats': ['Fluffy', 'Sheru Khan']}
```