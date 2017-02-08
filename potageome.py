from dico_appartenance import appartenance
from dico_plantes_categories import plantes
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
template = env.get_template('potageome.html')
output_from_parsed_template = template.stream(plantes=plantes, appartenance=appartenance).dump('potageome_rendered.html')