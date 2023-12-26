from pathlib import Path
from datetime import datetime as dt
from collections import defaultdict

ASSETS = sorted(Path("./assets/").glob("*.txt"))
PROB_DIR = Path("./problems")


def parse_problem(prob: str):
    date = prob.stat().st_mtime
    date = dt.utcfromtimestamp(date)
    
    prob = prob.stem.split("_")
    prob = list(map(lambda x: x.capitalize(), prob))
    return "- " + " ".join(prob), date


def fetch_problems(base_dir: Path = PROB_DIR) -> str:
    problems = sorted(filter(lambda x: x.is_dir(),
                             base_dir.glob("*")))
    probs = defaultdict(list)    
    for p in problems:
        pt, pdt = parse_problem(p)
        probs[f"{pdt.year} {str(pdt.month).zfill(2)}"].append(pt)
    
    txt = "\n"
    for date_key, _probs in probs.items():
        txt = txt + f"### {date_key}\n"
        txt = txt + "\n".join(_probs)
        txt = txt + "\n"
    return txt


def get_readme() -> str:
    with open(ASSETS[0], mode="r") as f:
        txt = f.readlines()
    txt = "\n".join(txt)
    txt = txt + "\n## Solved Problems\n"
    txt += fetch_problems()
    return txt


def main():
    txt = get_readme()
    with open("README.md", mode="w") as f:
        f.write(txt)


if __name__=="__main__":
    txt = get_readme()
    print(txt)
    main()