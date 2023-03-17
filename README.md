# rabbit or wrench

This is a word game, usually played with a group of people, but recreated on
top of word embeddings to be player vs computer.

The way it works is you run `python ./app/main.py play` and are presented with
an interactive session. It should look like this:

```sh
$ python ./app/main.py play
>
```

Once that's open, start playing. The first move is always the same:

```sh
$ python ./app/main.py play
> choose rabbit wrench
rabbit
```

The computer will tell you which of the two words you provide is closer to the
secret word (don't worry--it only ever chooses a common noun). From here, you
just keep guessing. An example session looks like this:

```sh
> choose rabbit wrench
rabbit
> choose rabbit apple
apple
> choose apple pear
pear... you got it!
```

## Setup

To get setup, first make a virtualenv using python3. Then install the
requirements and run the game from within the venv.

```sh
$ virtualenv venv --python python3
$ source ./venv/bin/active
$ pip install -r requirements.txt
$ python ./app/main.py play
```
