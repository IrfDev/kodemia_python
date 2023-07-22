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

When you create a new subclass, you'll ned to include a `super()` constructor, where you can call the parent class, including his [dunder methods](#dunder-methods). Where you can call his corresponding `__init__` method to intialize, the `__init__` declaration consoleould look like this 

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

### Installing packages from a file: 

```````console 
pip install -r FILE_TO_READ_PACKAGES_FROM
````````

## venv 

Module to create virtual environments for python. It basically creates the required files for python execution, including pip packages. 

The initial command to create a new virtual env is: 

``````````console
python -m venv INITIAL_DIRECTORY

``````````

Each environment can be activated or deactivated

#### To activate: 

``````````console
source PATH/OF/YOUR/PROJECT/bin/activate
``````````
where `bin/activate` is the executable of the python environment 


#### To deactivate:

``````````console
deactivate
``````````

Preferably iniside the venv directory


#### Init with a specific python version: 
By default the python version on your new venv it'll be the one you already had installed on your machine.

But you can specify a python version by passing a flag:

``````````console
python -3.7 -m venv test_env
``````````
Where the flag `-3.7` is the version you want to set for you new virtual environment.

#### ipython
Super interpreter for python. 

It includes a repl with an interpreter which can help to:
- Debug 
- Try or demo some code inside your terminal
