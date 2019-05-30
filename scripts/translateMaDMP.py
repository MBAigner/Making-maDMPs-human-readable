import json
import jinja2
import pdfkit

input = "../maDMPs/sample.json"
output = "../hrDMPs/out"
template = "FWF"

def get_contact(ma_dmp):
    return ma_dmp["dmp"]["contact"]["name"], \
           ma_dmp["dmp"]["contact"]["mail"], \
           ma_dmp["dmp"]["contact"]["contact_id"]["contact_id"], \
           ma_dmp["dmp"]["contact"]["contact_id"]["contact_id_type"]


def parse_contact(ma_dmp):
    name, mail, id, type = get_contact(ma_dmp)
    return "The contact person of the project is " + name + ". They can be reached on the mail " \
           + mail + ". Their " + type + " is " + id + "."


def create_html(text):
    global template
    global output

    templateLoader = jinja2.FileSystemLoader(searchpath="../templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template_" + template.lower() + ".html"
    real_template = templateEnv.get_template(TEMPLATE_FILE)

    outputText = real_template.render(contact=text)
    html_file = open(output + ".html", 'w')
    html_file.write(outputText)
    html_file.close()


with open(input, 'r') as f:
    ma_dmp = json.load(f)

contact = parse_contact(ma_dmp)
print(contact)
create_html(contact)

