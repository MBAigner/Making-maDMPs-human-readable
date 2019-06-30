import json
import jinja2
import pdfkit
# import wkhtmltopdf
# import subprocess

input = "../maDMPs/sample.json" # Input file
output = "../hrDMPs/out" # Output file (html + pdf)
# Chosen template
template = "FWF" # "FWF"

pdf_options = {
    "page-size": "A4",
    "orientation": "portrait"
}

# TODO more things depending on template
if template == "FWF":
    pdf_options["orientation"] = "landscape"


def get_contact(ma_dmp):
    return ma_dmp["dmp"]["contact"]["name"], \
           ma_dmp["dmp"]["contact"]["mail"], \
           ma_dmp["dmp"]["contact"]["contact_id"]["contact_id"], \
           ma_dmp["dmp"]["contact"]["contact_id"]["contact_id_type"]


def parse_contact(ma_dmp):
    name, mail, id, type = get_contact(ma_dmp)
    return "The contact person of the project is " + name + ". They can be reached on the mail " \
           + mail + ". Their " + type + " is " + id + "."


def create_html(text, template, output):
    """
    Creates an HTML file with given template and content.
    :param text: Demo, just contact information
    :param template: FWF or Horizon template file
    :param output: Name of the output file
    :return: Name of the output file (html)
    """

    # TODO uncomment this for orginal DMP format (right now difficult with differing section sizes)
    #templateLoader = jinja2.FileSystemLoader(searchpath="../templates/new")
    templateLoader = jinja2.FileSystemLoader(searchpath="../templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template_" + template.lower() + ".html"
    real_template = templateEnv.get_template(TEMPLATE_FILE)

    outputText = real_template.render(contact=text)
    html_file = open(output + ".html", "w")
    html_file.write(outputText)
    html_file.close()

    return output + ".html"


def create_pdf(html, options):
    """
    Converts a given HTML file into a PDF.
    :param html: HTML file
    :param options: options for formatting the PDF file
    :return: name of the resulting pdf file
    """

    # TODO: we will change this path, or use an other library for converting PDF!
    # TODO: otherwise just say that wkhtmltopdf needs to be pre-installed (and how) and added to windows path
    path_wkthmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    pdfkit.from_file(html, html.replace(".html", ".pdf"), configuration=config, options=options)
    return html + ".pdf"


with open(input, 'r') as f:
    ma_dmp = json.load(f)


contact = parse_contact(ma_dmp)
print(contact)
html_file = create_html(contact, template, output)
print(html_file)
pdf_file = create_pdf(html_file, pdf_options)
print(pdf_file)
