import yaml


def test_yaml():
    with open("./datas/cacl.yml", "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        print(datas["add"]["datas"])


a: int = None
a.
