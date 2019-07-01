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
    hostInfo = ""
    hostInfoExtended = ""
    generalDescription = ""
    metaIdentifiers = ""
    FAIRDataset = ""
    metaInfo = ""
    DataQuality = ""
    backupData = ""
    licenseInfo = ""
    accessInfo = ""

    for dataset in datasets:
        DataQuality = DataQuality + dataset.get("data_quality_assurance")
        dataset_ids = dataset.get("dataset_id", [])
        datasetTitle = dataset["title"]
        keywords = dataset.get("keyword", [])
        datasetLanguage = dataset.get("language", "")
        datasetLanguage = "english" if datasetLanguage == "en" else datasetLanguage
        description = dataset.get("description", "")
        distributions = dataset.get("distribution", []) # can be zero!
        generalDescription = generalDescription + "Dataset - " + datasetTitle + ": " + description + "\n"

        for dataset_id in dataset_ids:
            identifiers = identifiers + "The dataset " + datasetTitle + " can be identified using " + dataset_id["dataset_id"] + ", which is an " + dataset_id["dataset_id_type"] + ".\n"

        FAIRDataset = identifiers
        if datasetLanguage != "":
            FAIRDataset = FAIRDataset + "The dataset is in " + datasetLanguage + ". "
        if keywords:
            FAIRDataset = FAIRDataset + "It can be found using the following keywords: " + (", ".join(['"' + str(x) + '"' for x in keywords]) + ".\n")

        metadatas = dataset.get("metadata", [])
        for metadata in metadatas:
            metaDescrip = metadata.get("description", "")
            metaLang = metadata["language"]
            metaLang = "English" if metaLang == "en" else metaLang
            metaId = metadata["metadata_id"]["metadata_id"]
            metaIdType = metadata["metadata_id"]["metadata_id_type"]

            if metaLang != "":
                metaInfo = metaInfo + "The metadata is in " + metaLang + ". "
            if metaInfo != "":
                metaInfo = metaInfo + "The metadata " + metaDescrip + " "

            metaIdentifiers = metaIdentifiers + "The dataset " + datasetTitle + " uses the following standard (referenced by " + metaIdType + ") " + metaId + ".\n"

        for distribution in distributions:
            access_url = distribution.get("access_url", "")
            available_till = distribution.get("available_till", "")
            data_access = distribution.get("data_access", "")
            download_url = distribution.get("download_url", "")

            if access_url != "":
                accessInfo = accessInfo + "One can access the data through " + access_url + ". "
            if data_access != "":
                accessInfo = accessInfo + "The data will be available as " + data_access + " data. "
            if available_till != "":
                accessInfo = accessInfo + "The dataset will be available until " + available_till + ". "
            if download_url != "":
                accessInfo = accessInfo + "One can download the data from " + download_url + ".\n"

            licenses = distribution.get("license", "")
            for license in licenses:
                if license != "":
                    license_ref = license["license_ref"]
                    start_date = license["start_date"]

                    licenseInfo = licenseInfo + "The dataset is licensed under " + license_ref + " starting at " + start_date + ".\n"

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
                backup__frequency = host.get("backup__frequency", "")
                backup_type = host.get("backup_type", "")
                geo_location = host.get("geo_location", "")

                if backup__frequency != "" and backup_type != "":
                    backupData = backupData + "The data is backed up " + backup__frequency + " on " + backup_type + ".\n"
                if backup__frequency == "" and backup_type != "":
                    backupData = backupData + "The data is backed up on " + backup_type + ".\n"
                if backup__frequency != "" and backup_type == "":
                    backupData = backupData + "The data is backed up " + backup__frequency + ".\n"

                hostDescription = host.get("description", "")
                hostDescriptionB = "(" + hostDescription + ") "
                support_versioning = host.get("support_versioning", "")
                if support_versioning == "yes":
                    result["versioning"] = result["versioning"] + "The selected repository " + hostDescriptionB + "provides versioning.\n"

                hostCertificate = host.get("certified_with", "")
                hostPids = host.get("pid_system", [])
                hostInfo = hostInfo + result["versioning"]
                for hostPid in hostPids:
                    hostInfo = hostInfo + "The host can be identified with " + hostPid + ". "

                if hostCertificate != "":
                    hostInfo = hostInfo + "Furthermore the host is certified with " + hostCertificate + ".\n"

                if geo_location != "":
                    hostInfoExtended = hostInfo + "The host can is located in " + geo_location + ".\n"

        generalDescription = generalDescription + "\n"

    result["backupData"] = backupData
    result["DataQuality"] = DataQuality + "\n"
    result["FAIRDataset"] = FAIRDataset
    result["metaIdentifiers"] = metaIdentifiers
    result["metaInfo"] = metaInfo
    result["hostInfo"] = hostInfo
    result["hostInfoExtended"] = hostInfoExtended
    result["generalDescription"] = generalDescription
    result["identifiers"] = identifiers
    result["licenseInfo"] = licenseInfo
    result["accessInfo"] = accessInfo

    return result