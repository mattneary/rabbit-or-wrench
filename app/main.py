from sentence_transformers import SentenceTransformer, util
import click
import os
from click_repl import register_repl, exit
import random

model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

lines = []
with open('words.txt') as f:
    lines = [l.strip() for l in f.readlines()]

secret = random.choice(lines)
vec_secret = model.encode(secret)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('opt_a')
@click.argument('opt_b')
def choose(opt_a, opt_b):
    vec_a, vec_b = model.encode(opt_a), model.encode(opt_b)
    score_a, score_b = util.dot_score(vec_secret, vec_a), util.dot_score(vec_secret, vec_b)
    winner, wscore = max([(opt_a, score_a), (opt_b, score_b)], key=lambda pair: pair[1])
    score = wscore[0][0] # ready in case we want to print it
    if winner == secret:
        click.echo(f"{winner}... you got it!")
        exit()
    else:
        click.echo(f"{winner}")


@cli.command()
def giveup():
    click.echo(f"{secret}... you lose!")
    exit()


if __name__ == '__main__':
    register_repl(cli, name='play')
    cli()
