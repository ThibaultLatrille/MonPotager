from dico_appartenance import appartenance
from dico_plantes_categories import plantes
from dict2json import generate_js
import jinja2
from scss import parser
compress = False

generate_js()

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
template = env.get_template('potageome.html')
output_from_parsed_template = template.stream(plantes=plantes,
                                              appartenance=appartenance).dump('potageome_rendered.html')
css = open("potageome.css", "w")
css.write(parser.Stylesheet(options=dict(compress=compress)).load('potageome.css.scss'))
css.close()
