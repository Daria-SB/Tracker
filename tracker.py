import csv
import click
from typing import List, Dict

class Entry:
    def __init__(self, desc, time, tags):
        self.desc = desc
        self.time = time
        self.tags = tags 


    def __repr__(self):
        return f"Entry(description={self.desc!r}, duration={self.time!r}, tag={self.tags!r})"
     
    
    def __str__(self):
        tags = [f'#{t}' for t in self.tags]
        tags = " ".join(tags)
        return f"{self.desc}  ({self.time}  min)  {tags}"


def create_entry(row):
    tags = row["tags"].split(" ")
    tags = [t.strip() for t in tags]
    entry = Entry(desc = row["desc"].strip(), time = int(row["time"].strip()), tags = tags)
    return entry


def load_entries(csv_file):
    with open (csv_file) as stream:
        reader = csv.DictReader(stream) 
        entries = [create_entry(row) for row in reader]
    return entries 


def tag_counter(entries):
    tags = {t for e in entries for t in e.tags}
    report = {}
    for tag in tags:
        total = sum(e.time for e in entries if tag in e.tags)
        report[tag] = total
    return report


def print_raport_by_tags(time_by_tags):
    print("TOTAL TIME    TAG")
    for tag, time in time_by_tags.items():
        print(f"{time:10}   #{tag}")


@click.command()
@click.argument("csv_file")


def main(csv_file):
    entries = load_entries(csv_file)
    raport = tag_counter(entries)
    print_raport_by_tags(raport) 


if __name__ == "__main__":
    main()