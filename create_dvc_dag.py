import click
from dvc.repo import Repo


@click.command()
@click.argument("data_path")
@click.argument("out")
def create_dag(data_path: str, out: str) -> None:
    repo = Repo()
    repo.run(cmd=f"python train_model.py {data_path} {out}", deps=[data_path], outs=[out],
             fname=out + ".dvc")


if __name__ == "__main__":
    create_dag()
