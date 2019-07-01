def get_contact(ma_dmp):
    return ma_dmp["dmp"]["contact"]["name"], \
           ma_dmp["dmp"]["contact"]["mail"], \
           ma_dmp["dmp"]["contact"]["contact_id"]["contact_id"], \
           ma_dmp["dmp"]["contact"]["contact_id"]["contact_id_type"]


def parse_contact(ma_dmp):
    name, mail, id, type = get_contact(ma_dmp)
    return "The contact person of the project is " + name + ". They can be reached on the mail " \
           + mail + ". Their " + type + " is " + id + "."


def parse_cost(ma_dmp):
    costs = ma_dmp["dmp"].get("cost", None)

    if costs is None:
        return ""

    resultString = ""
    for cost in costs:
        currencyCode = cost.get("currency_code", "")
        description = cost.get("description", "")
        title = cost["title"]
        value = cost.get("value", "")
        resultString = resultString + "There will be costs for " + title + "" + \
                       ("." if description == "" else " (" + description + ").") + \
                       ("" if value == "" else " These procedures will cost " + str(value) + currencyCode) + ".\n"

    return resultString

def parse_dataset(ma_dmp):
    datasets = ma_dmp["dmp"]["dataset"]

    result = {}
    result["versioning"] = ""
    identifiers = ""
    generalDescription = ""

    for dataset in datasets:
        dataset_ids = dataset.get("dataset_id", [])
        datasetTitle = dataset["title"]
        description = dataset.get("description", "")
        distributions = dataset.get("distribution", []) # can be zero!
        generalDescription = generalDescription + "Dataset - " + datasetTitle + ": " + description + "\n"
        identifiers = identifiers + "The dataset " + datasetTitle + " is identified using " + dataset_ids["dataset_id"] + ", which is an " + dataset_ids["dataset_id_type"] + ".\n"
        for distribution in distributions:
            distributionTitle = distribution["title"]
            format = distribution.get("format", "")
            byte_size = distribution.get("byte_size", "")
            if format == "" and byte_size == "":
                generalDescription = generalDescription + distributionTitle + " is one of the datasets distributions.\n"
            elif format == "" and byte_size != "":
                generalDescription = generalDescription + "The distribution " + distributionTitle + " of the dataset is " + str(byte_size) + "bytes large.\n"
            elif format != "" and byte_size == "":
                generalDescription = generalDescription + "The distribution " + distributionTitle + " of the dataset is provided in the format " + \
                    format + ".\n"
            else:
                generalDescription = generalDescription + "The distribution " + distributionTitle + " of the dataset is provided in the format " + \
                    format + " and is " + str(byte_size) + "bytes large.\n"

            host = distribution.get("host", None)
            if not(host is None):
                hostDescription = host.get("description", "")
                hostDescriptionB = "(" + hostDescription + ") "
                support_versioning = host.get("support_versioning", "")
                if support_versioning == "yes":
                    result["versioning"] = result["versioning"] + "The selected repository " + hostDescriptionB + "provides versioning.\n"

        generalDescription = generalDescription + "\n"

    result["generalDescription"] = generalDescription
    result["identifiers"] = identifiers

    return result