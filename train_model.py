import click
import pandas as pd


@click.command()
@click.argument("data_path")
@click.argument("out")
def train_model(data_path: str, out: str) -> None:
    data = pd.read_csv(data_path)
    data["c"] = data["a"] + data["b"]
    data.to_csv(out)


if __name__ == "__main__":
    train_model()
