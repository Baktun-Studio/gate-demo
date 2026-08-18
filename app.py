"""Tiny demo service: reads a YAML config and serves it."""
import yaml


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    print(load_config("config.yml"))
