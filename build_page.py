import csv
import pathlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output_folder")

args = parser.parse_args()

args.input = pathlib.Path(args.input)
args.output_folder = pathlib.Path(args.output_folder)

# TODO: make the search nice
content = """
# Software

These are the software projects produced by the EISCAT user community.

<div class="search-container">
    <div class="search-button">
        <label class="md-search__icon md-icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
    </div>
    <input type="text" id="SearchInput" name="Search" class="search-input"/>
</div>


<div class="grid cards" markdown id="DataContainer">


"""

fmt = """

-   __`{name}`__

    ---

    ??? abstract "{description}"

        {abstract}

    Status: {status}
    Contact: {contact}
    Tags: {tags}

    {links}

"""

with open(args.input, "r") as fh:
    data = csv.DictReader(fh)
    for row in data:
        row["links"] = "\n\n    ".join(row["links"].split(";"))
        content += fmt.format(**row)

content += """

</div>

"""
with open(args.output_folder / (args.input.stem + ".md"), "w") as fh:
    fh.write(content)
