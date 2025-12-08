import yaml

def load_data():
    with open("_data/cv.yaml", "r", encoding="utf-8") as file:
        cv_data = yaml.safe_load(file)
        cv_data["total_assigned"] = sum(
            item["assigned"] for item in cv_data.get("funding", []))

data = load_data()
with open("_data/cv.yaml", "w", encoding="utf-8") as file:
    yaml.dump(data, file, allow_unicode=True)

