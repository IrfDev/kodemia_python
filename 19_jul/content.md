## Dunder methods: 
#### File: ./dunders.py

Dunder methods are special methods pre-binded to an object, it can be a class, or a dict, or other type of objects

You can override dunder methods

Commonly you'll update `__str__`, `__init__` and `__repr__`. 

`__repr__`: Will define the representation of the value of the instance when you save it.



## Subclass: 
#### File: ./subclass.py

You can have one class and different instances and subclasses. 
You can also create classes based on multiple parents. 

The syntaxis for create new subclasses is: `User(*PARENT_INSTANCES)` where `*PARENT_INSTANCES` is a tuple of parent classes

When you create a new subclass, you'll ned to include a `super()` constructor, where you can call the parent class, including his [dunder methods](#dunder-methods). Where you can call his corresponding `__init__` method to intialize, the `__init__` declaration should look like this 

```````python
 def _init_(self, hair_color, eye_color):
        #super()=parent class  
        super()._init_(2, 2, hair_color)
        #  You can't access properties before initiailization
        self.eye_color = eye_color
```````


## Remote imports and package manager

The common package manager for python is [pypip or pip](https://pypi.org/).

Where you can call different packages and import them as you need it
