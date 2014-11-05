import yaml2py


if __name__ == "__main__":
    pipeline = yaml2py.from_yaml("config.yaml")
    print(pipeline)
