import json

input = "../maDMPs/sample.json"
output = "../hrDMPs/out.pdf"
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

with open(input, 'r') as f:
    ma_dmp = json.load(f)

print(parse_contact(ma_dmp))

