#!/usr/bin/env python3
import argparse
from glob import glob
from association2json import generate_js
import jinja2
from jsmin import jsmin
import sass
import os

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
ENDC = '\033[0m'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Minifying the .js and .css with -c option")
    parser.add_argument('-c', action='store_true')
    args = parser.parse_args()

    months, plants, appartenance, examples, categories, cat_plants, cat_animals, interactions = generate_js("js/data.js")

    print(months['Carotte'])


    minified = ""
    if args.c:
        minified = "min."
        for js_path in ["js/MonPotager.js", "js/data.js"]:
            with open(js_path, 'r') as js_file:
                jsminified = jsmin(js_file.read())
                jsminified_file = open(js_path.replace('.js', ".min.js"), "w")
                jsminified_file.write(jsminified)
                jsminified_file.close()
                print(OKBLUE + "Minifying " + js_path + ENDC)
    else:
        print(OKBLUE + ".js and .css not minified, use -c option if you wish to compress files." + ENDC)

    css = open("css/MonPotager." + minified + "css", "w")
    css.write(sass.compile(filename='MonPotager.css.scss', output_style=('compressed' if args.c else "nested")))
    css.close()

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
    template = env.get_template('MonPotager.html')

    first_letter = sorted(set([name[0].upper() for key, name in plants.items() if (appartenance[key] in cat_plants)]))
    sorted_appartenance = sorted(appartenance.items(), key=lambda pl: plants[pl[0]].lower())

    output_from_parsed_template = template.stream(months=months,
                                                  plants=plants,
                                                  examples=examples,
                                                  minified=minified,
                                                  cat_plants=cat_plants,
                                                  cat_animals=cat_animals,
                                                  categories=categories,
                                                  first_letter=first_letter,
                                                  interactions=interactions,
                                                  appartenance=sorted_appartenance).dump('index.html')
    print(OKGREEN + "Application generated.\nOpen the file {0}/index.html to open the application.".format(
        os.getcwd()) + ENDC)
