from interaction2json import generate_js
import jinja2
import sass

plantes, appartenance = generate_js()

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
template = env.get_template('potageome.html')
output_from_parsed_template = template.stream(plantes=plantes,
                                              appartenance=sorted(appartenance.items(),
                                                                  key=lambda pl: plantes[pl[0]].lower())
                                              ).dump('potageome_rendered.html')

css = open("potageome.css", "w")
print(sass.compile(filename='potageome.css.scss'))
css.write(sass.compile(filename='potageome.css.scss'))
css.close()
