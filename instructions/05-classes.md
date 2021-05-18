## Classes, objects and dunders

In this section we'll introduce
how to make classes,
and how to take advantage of some of Python's in built features
by writing specially named methods.

## Classes

You create classes using the `class` keyword.

To allow someone to create instances of the class
you need to define an `__init__()` method.

_NOTE:_ `__init__()` is what's known as a 'dunder' method
(double underscore).
Dunder methods have a special meaning to Python
and are used by the interpreter itself.

For example, here is a class called City
with name and population instance attributes.

``` python
class City:
    # All instance methods take `self` as an argument
    def __init__(self, name, population):
        self.name = name
        self.population = population
```

You can create an instance of the class
by using the class name
and access an instances elements using the `.` operator.

```
>>> welly.name
'Wellington'
>>> welly.population
416828
```

## Instance methods

Just like the `__init__()` method,
you can create methods that affect object instances
by passing the method the `self` parameter.

``` python
class City:
    def __init__(self, name, population):
        ...
    
    def grow(self, people):
        self.population += people

    def shrink(self, people):
        if people > self.population:
            raise ValueError("A city can't have a negative population")
        
        self.population -= people
```

## Dunder methods

Now, we have the city object.
What happens if we try and print it to the terminal
to inspect its contents
like we've been doing for other types?

```
>>> welly
<__main__.City object at 0x7f0c2a1bd810>
```

That's not very useful is it?

We can make this better by implementing the `__str()__` and `__repr__()` methods.
We use `__str__()` to generate some human readable text
and we use `__repr__()` to give a more "official" string
useful for debugging.

``` python
def __repr__(self):
    return f"City(name={self.name}, population={self.population})"

def __str__(self):
    return f"{self.name}, population: {self.population}"
```

Now when we try and inspect the contents
or convert to a string
we get something actually useful.

```
>>> welly
City(name=Wellington, population=416828)
>>> str(welly)
Wellington, population: 416828
```
