# AutoCase (WIP:Expect Major Changes)

Automatic AI based (optional) Camel / Snake / Pascal / Kebab / Train(Title) / Upper / Lower Case Conversion

# Python Installation
```bash
pip install autocase
```

# Usage
## Basic Usage
```python
from autocase import AutoCase

string = "Hello World"
camel = AutoCase(string).camel() # helloWorld
snake = AutoCase(string).snake() # hello_world
pascal = AutoCase(string).pascal() # HelloWorld
kebab = AutoCase(string).kebab() # hello-world
train = AutoCase(string).train() # Hello-World
upper = AutoCase(string).upper() # HELLO WORLD
lower = AutoCase(string).lower() # hello world
```

## AI Based Conversion
```python
from autocase import AutoCase

string = "helloworld"
camel = AutoCase(string).camel(ai=True,outputs=3) # [helloWorld, hellOworld, hellOWorld]
snake = AutoCase(string).snake(ai=True,outputs=3) # [hello_world, hell_oworld, hell_o_world]
pascal = AutoCase(string).pascal(ai=True,outputs=3) # [HelloWorld, HellOworld, HellOWorld]
kebab = AutoCase(string).kebab(ai=True,outputs=3) # [hello-world, hell-oworld, hell-o-world]
train = AutoCase(string).train(ai=True,outputs=3) # [Hello-World, Hell-Oworld, Hell-O-World]
upper = AutoCase(string).upper(ai=True,outputs=3) # [HELLO WORLD, HELL OWORLD, HELL O WORLD]
lower = AutoCase(string).lower(ai=True,outputs=3) # [hello world, hell oworld, hell o world]
```

## Dictionary Based Conversion
```python
from autocase import AutoCase

word_list = ["hello","world","hell"]

string = "helloworld"
camel = AutoCase(string,dictionary=word_list).camel(outputs=3) # [helloWorld, hellWorld, hellWorld]
snake = AutoCase(string,dictionary=word_list).snake(outputs=3) # [hello_world, hell_world, hell_world]
pascal = AutoCase(string,dictionary=word_list).pascal(outputs=3) # [HelloWorld, HellWorld, HellWorld]
kebab = AutoCase(string,dictionary=word_list).kebab(outputs=3) # [hello-world, hell-world, hell-world]
train = AutoCase(string,dictionary=word_list).train(outputs=3) # [Hello-World, Hell-World, Hell-World]
upper = AutoCase(string,dictionary=word_list).upper(outputs=3) # [HELLO WORLD, HELL WORLD, HELL WORLD]
lower = AutoCase(string,dictionary=word_list).lower(outputs=3) # [hello world, hell world, hell world]
```






