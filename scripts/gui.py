import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

from scripts.parsingMethods import *

import json
import jinja2
import pdfkit
import os

DEBUG = True


###########################
# Basic UI elements

root = tk.Tk()
root.title("Making-maDMPs-human-readablse")
root.style = Style()
root.style.theme_use("alt")
#('clam', 'alt', 'default', 'classic')

title = tk.Label(root, text="Making-maDMPs-human-readable",
                 font="Helvetica 16 bold")
title.grid(row = 0, columnspan=6, sticky = N)

#############################
# GUI Elements

selectedTemplate = None

# FWF
dataOfficerLabel = None
dataDescriptionLabel = None
dataDescriptionLabel1 = None
docMetaLabel = None
docMetaLabel1 = None
docMetaLabel2 = None
docMetaLabel3 = None
dataSharingLabel = None
dataSharingLabel1 = None
dataSharingLabel2 = None
ethicalLabel = None
ethicalLabel1 = None
ethicalLabel2 = None
generatedDataLabel = None

dataOfficerText = None
dataDescriptionText1 = None
docMetaText1 = None
docMetaText2 = None
docMetaText3 = None
dataSharingText1 = None
dataSharingText2 = None
ethicalText1 = None
ethicalText2 = None
generatedDataText = None

# Horizon
abstractLabel = None
dataDescriptionLabel1 = None
fairLabel1 = None
fairLabel2 = None
fairLabel3 = None
fairLabel4 = None
resourceLabel = None
securityLabel = None
ethicalLabel = None
otherLabel = None

abstractText = None
dataDescriptionText1 = None
fairText1 = None
fairText2 = None
fairText3 = None
fairText4 = None
resourceText = None
securityText = None
ethicalText = None
otherText = None

#############################
# GUI Functions

def chooseMaDMP(event=None):
    """
    Upload dialog for maDMPs
    """
    file_name = filedialog.askopenfilename(title = "Select maDMP file",
                                           filetypes = (("JSON files","*.json"),("all files","*.*")))
    if DEBUG:
        print('Selected:', file_name)
    fileEntry.insert(0, file_name)


def chooseTemplate(event=None):
    """
    Update GUI according to template
    """
    global selectedTemplate
    if selectedTemplate is not None: # clears GUI
        destroyOldTemplate(templatesCombo.get())

    selectedTemplate = templatesCombo.get()
    if selectedTemplate == "FWF": # load FWF template
        createFWFItems()
        createModificationItems(11)

    else: # load Horizon template
        createHorizonItems()
        createModificationItems(15)


def destroyOldTemplate(new_template):
    """
    Clears the whole template environment
    """
    saveButton.destroy()
    fillButton.destroy()

    if new_template != "FWF": # Clear FWF
        dataOfficerLabel.destroy()
        dataDescriptionLabel.destroy()
        dataDescriptionLabel1.destroy()
        docMetaLabel.destroy()
        docMetaLabel1.destroy()
        docMetaLabel2.destroy()
        docMetaLabel3.destroy()
        dataSharingLabel.destroy()
        dataSharingLabel1.destroy()
        dataSharingLabel2.destroy()
        ethicalLabel.destroy()
        ethicalLabel1.destroy()
        ethicalLabel2.destroy()
        generatedDataLabel.destroy()

        dataOfficerText.destroy()
        dataDescriptionText1.destroy()
        docMetaText1.destroy()
        docMetaText2.destroy()
        docMetaText3.destroy()
        dataSharingText1.destroy()
        dataSharingText2.destroy()
        ethicalText1.destroy()
        ethicalText2.destroy()
        generatedDataText.destroy()

    else: # Clear Horizon
        abstractLabel.destroy()
        dataDescriptionLabel1.destroy()
        fairLabel1.destroy()
        fairLabel2.destroy()
        fairLabel3.destroy()
        fairLabel4.destroy()
        resourceLabel.destroy()
        securityLabel.destroy()
        ethicalLabel.destroy()
        otherLabel.destroy()

        abstractText.destroy()
        dataDescriptionText1.destroy()
        fairText1.destroy()
        fairText2.destroy()
        fairText3.destroy()
        fairText4.destroy()
        resourceText.destroy()
        securityText.destroy()
        ethicalText.destroy()
        otherText.destroy()


def fillInTemplate(event=None):
    """
    Fills in data from selected JSON file
    """
    file_name = fileEntry.get()
    if DEBUG:
        print("Filling in data from " + str(file_name))

    if not os.path.exists(file_name):
        print("Selected does not exist!")
    else:
        # File exists - start parsing here!
        print("Processing JSON :))")
        # TODO this is just one use case !!
        if selectedTemplate == "FWF":
            with open(file_name, 'r') as f:
                ma_dmp = json.load(f)

            datasetData = parse_dataset(ma_dmp)
            dataDescriptionText1.delete("1.0", END)
            dataDescriptionText1.insert(END, datasetData["generalDescription"])
            dataDescriptionText1.insert(END, datasetData["versioning"])

            docMetaText1.delete("1.0", END)
            docMetaText1.insert(END, datasetData["metaIdentifiers"])

            docMetaText2.delete("1.0", END)
            docMetaText2.insert(END, datasetData["FAIRDataset"])


            contact_data = parse_contact(ma_dmp)
            dataOfficerText.delete("1.0", END)
            dataOfficerText.insert(END, contact_data)

            cost_data = parse_cost(ma_dmp)
            dataSharingText2.delete("1.0", END)
            dataSharingText2.insert(END, cost_data)



def resetTemplate(event=None):
    """
    Resets all DMP values to default
    """
    # TODO change this to modified DMP, not original values
    # TODO -> most likely just new fill-in
    global selectedTemplate
    selectedTemplate = None
    chooseTemplate()


def saveDMP(event=None):
    """
    Fills HTML file with content of DMP
    Generates PDF document out of HTML file
    """
    f = filedialog.asksaveasfile(mode='w', defaultextension=".pdf")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return

    html = create_html(template=selectedTemplate, output=f.name.replace(".pdf", ""))
    print("Stored HTML successfully as " + str(html))
    pdf = create_pdf(html=html)
    print("Stored PDF successfully as " + str(pdf))


def createModificationItems(row):
    """
    Adds buttons for DMP modification and saving
    :param row: row where the buttons will be placed
    """
    global saveButton
    global fillButton

    # Modify DMP text
    fillButton = tk.Button(root, text='Fill in DMP data', command=fillInTemplate, width = 30)
    fillButton.grid(row=row, column=0, columnspan = 3, sticky=S)


    # Save result
    saveButton = tk.Button(root, text='Save DMP', command=saveDMP, width = 30)
    saveButton.grid(row=row, column=3, columnspan=3, sticky=S)


def createHorizonItems():
    """
    Fills in all GUI items necessary for Horizon 2020 template
    """
    global abstractLabel
    global dataDescriptionLabel1
    global fairLabel1
    global fairLabel2
    global fairLabel3
    global fairLabel4
    global resourceLabel
    global securityLabel
    global ethicalLabel
    global otherLabel

    global abstractText
    global dataDescriptionText1
    global fairText1
    global fairText2
    global fairText3
    global fairText4
    global resourceText
    global securityText
    global ethicalText
    global otherText

    abstractLabel = tk.Label(root, text="Abstract", font="Helvetica 10")
    abstractLabel.grid(row=4, column=0, sticky=W)
    abstractText = tk.Text(root, width=70, height=5)
    abstractText.insert(END, "Title\nA Data Management Plan created using DMPonline\nCreator: \n"
                             "Affiliation: \nTemplate: European Commission (Horizon 2020)\n"
                             "Last modified: ")
    abstractText.grid(row=5, column=0, columnspan=2, sticky=W)

    dataDescriptionLabel1 = tk.Label(root, text="1. Data Summary", font="Helvetica 10")
    dataDescriptionLabel1.grid(row=6, column=0, columnspan = 2, sticky=W)
    dataDescriptionText1 = tk.Text(root, width=70, height=5)
    dataDescriptionText1.insert(END,"State the purpose of the data collection/generation\n"
                                    "Explain the relation to the objectives of the project\n"
                                    "Specify the types and formats of data generated/collected\n"
                                    "Specify if existing data is being re-used (if any) \n"
                                    "Specify the origin of the data \n"
                                    "State the expected size of the data (if known) \n"
                                    "Outline the data utility: to whom will it be useful")
    dataDescriptionText1.grid(row=7, column=0, columnspan=3, sticky=W)

    fairLabel1 = tk.Label(root, text="2.1 Making data findable, including provisions for metadata [FAIR data] ", font="Helvetica 10")
    fairLabel1.grid(row=8, column=0, columnspan = 2,sticky=W)
    fairText1 = tk.Text(root, width=70, height=5)
    fairText1.grid(row=9, column=0, columnspan=3, sticky=W)
    fairText1.insert(END, "Outline the discoverability of data (metadata provision)\n"
                          "Outline the identifiability of data and refer to standard identification mechanism. Do you make use of persistent and unique identifiers such as Digital Object Identifiers?\n"
                          "Outline naming conventions used\n"
                          "Outline the approach towards search keyword\n"
                          "Outline the approach for clear versioning\n"
                          "Specify standards for metadata creation (if any). If there are no standards in your discipline describe what metadata will be created and how")

    fairLabel2 = tk.Label(root, text="2.2 Making data openly accessible [FAIR data]", font="Helvetica 10")
    fairLabel2.grid(row=10, column=0, columnspan = 2, sticky=W)
    fairText2 = tk.Text(root, width=70, height=5)
    fairText2.grid(row=11, column=0, columnspan=3, sticky=W)
    fairText2.insert(END,
                     "Specify which data will be made openly available? If some data is kept closed provide rationale for doing so\n"
                     "Specify how the data will be made available\n"
                     "Specify what methods or software tools are needed to access the data? Is documentation about the software needed to access the data included? Is it possible to include the relevant software (e.g. in open source code)?\n"
                     "Specify where the data and associated metadata, documentation and code are deposited\n"
                     "Specify how access will be provided in case there are any restrictions")

    fairLabel3 = tk.Label(root, text="2.3 Making data interoperable [FAIR data]", font="Helvetica 10")
    fairLabel3.grid(row=12, column=0, sticky=W)
    fairText3 = tk.Text(root, width=70, height=5)
    fairText3.grid(row=13, column=0, columnspan=3, sticky=W)
    fairText3.insert(END, "Assess the interoperability of your data. Specify what data and metadata vocabularies, standards or methodologies you will follow to facilitate interoperability. \n"
                          "Specify whether you will be using standard vocabulary for all data types present in your data set, to allow inter-disciplinary interoperability? If not, will you provide mapping to more commonly used ontologies?")

    fairLabel4 = tk.Label(root, text="2.4 Increase data re-use (through clarifying licenses) [FAIR data]",
                          font="Helvetica 10")
    fairLabel4.grid(row=4, column=2, sticky=W)
    fairText4 = tk.Text(root, width=70, height=5)
    fairText4.grid(row=5, column=2, columnspan=3, sticky=W)
    fairText4.insert(END,
                     "Specify how the data will be licenced to permit the widest reuse possible\n"
                     "Specify when the data will be made available for re-use. If applicable, specify why and for what period a data embargo is needed\n"
                     "Specify whether the data produced and/or used in the project is useable by third parties, in particular after the end of the project? If the re-use of some data is restricted, explain why\n"
                     "Describe data quality assurance processes\n"
                     "Specify the length of time for which the data will remain re-usable")

    resourceLabel = tk.Label(root, text="3. Allocation of resources", font="Helvetica 10")
    resourceLabel.grid(row=6, column=2, sticky=W)
    resourceText = tk.Text(root, width=70, height=5)
    resourceText.grid(row=7, column=2, columnspan=3, sticky=W)
    resourceText.insert(END,
                     "Estimate the costs for making your data FAIR. Describe how you intend to cover these costs\n"
                     "Clearly identify responsibilities for data management in your project\n"
                     "Describe costs and potential value of long term preservation")

    securityLabel = tk.Label(root, text="4. Data security", font="Helvetica 10")
    securityLabel.grid(row=8, column=2, sticky=W)
    securityText = tk.Text(root, width=70, height=5)
    securityText.grid(row=9, column=2, columnspan=3, sticky=W)
    securityText.insert(END,
                        "Address data recovery as well as secure storage and transfer of sensitive data")

    ethicalLabel = tk.Label(root, text="5. Ethical aspects", font="Helvetica 10")
    ethicalLabel.grid(row=10, column=2, sticky=W)
    ethicalText = tk.Text(root, width=70, height=5)
    ethicalText.grid(row=11, column=2, columnspan=3, sticky=W)
    ethicalText.insert(END,
                       "To be covered in the context of the ethics review, ethics section of DoA and ethics deliverables. Include references and related technical aspects if not covered by the former")


    otherLabel = tk.Label(root, text="6. Other", font="Helvetica 10")
    otherLabel.grid(row=12, column=2, sticky=W)
    otherText = tk.Text(root, width=70, height=5)
    otherText.grid(row=13, column=2, columnspan=3, sticky=W)
    otherText.insert(END,
                    "Refer to other national/funder/sectorial/departmental procedures for data management that you are using (if any)")


def createFWFItems():
    """
    Fills in all GUI items necessary for FWF template
    """
    global dataOfficerLabel
    global dataDescriptionLabel
    global dataDescriptionLabel1
    global docMetaLabel
    global docMetaLabel1
    global docMetaLabel2
    global docMetaLabel3
    global dataSharingLabel
    global dataSharingLabel1
    global dataSharingLabel2
    global ethicalLabel
    global ethicalLabel1
    global ethicalLabel2
    global generatedDataLabel

    global dataOfficerText
    global dataDescriptionText1
    global docMetaText1
    global docMetaText2
    global docMetaText3
    global dataSharingText1
    global dataSharingText2
    global ethicalText1
    global ethicalText2
    global generatedDataText


    dataOfficerLabel = tk.Label(root, text="Data Officer", font="Helvetica 10")
    dataOfficerLabel.grid(row=4, column=0, sticky=W)
    dataOfficerText = tk.Text(root, width=70, height=5)
    dataOfficerText.insert(END, "Who is responsible for the data management and "
                                "the DMP of the project (name/email address)?")
    dataOfficerText.grid(row=4, column=1, columnspan=2, sticky=W)

    dataDescriptionLabel = tk.Label(root, text="I Data Characteristics", font="Helvetica 10")
    dataDescriptionLabel.grid(row=5, column=0, sticky=W)

    dataDescriptionLabel1 = tk.Label(root, text="I.1 Description of the data", font="Helvetica 10")
    dataDescriptionLabel1.grid(row=6, column=0, sticky=W)
    dataDescriptionText1 = tk.Text(root, width=70, height=5)
    dataDescriptionText1.insert(END,
                                "What kinds of data/source code will be generated or reused (type, format, volume)? "
                                "How will the research data be generated and which methods will be used? "
                                "How will you structure the data and handle versioning? Who is the target audience?")
    dataDescriptionText1.grid(row=6, column=1, columnspan=2, sticky=W)

    docMetaLabel = tk.Label(root, text="II Documentation and Metadata", font="Helvetica 10")
    docMetaLabel.grid(row=7, column=0, sticky=W)

    docMetaLabel1 = tk.Label(root, text="II.1 Metadata standards", font="Helvetica 10")
    docMetaLabel1.grid(row=8, column=0, sticky=W)
    docMetaText1 = tk.Text(root, width=70, height=5)
    docMetaText1.insert(END, "What metadata standards (if any) will be in use and why? (see Digital Curation Centre)")
    docMetaText1.grid(row=8, column=1, columnspan=2, sticky=W)

    docMetaLabel2 = tk.Label(root, text="II.2 Documentation of data", font="Helvetica 10")
    docMetaLabel2.grid(row=9, column=0, sticky=W)
    docMetaText2 = tk.Text(root, width=70, height=5)
    docMetaText2.insert(END,
                        "What information is needed for the data to be findable, accessible, interoperable and re-usable (FAIR) in the future? Is the data machine-readable? How are you planning to document this information?")
    docMetaText2.grid(row=9, column=1, columnspan=2, sticky=W)

    docMetaLabel3 = tk.Label(root, text="II.3 Data quality control", font="Helvetica 10")
    docMetaLabel3.grid(row=10, column=0, sticky=W)
    docMetaText3 = tk.Text(root, width=70, height=5)
    docMetaText3.insert(END,
                        "What quality assurance processes will you adopt? How will the consistency and quality of data collection be controlled and documented? (This may include processes such as repeat samples or measurements, standardised data capture, peer review of data or representation with controlled vocabularies.")
    docMetaText3.grid(row=10, column=1, columnspan=2, sticky=W)

    dataSharingLabel = tk.Label(root, text="III Data Availability and Storage", font="Helvetica 10")
    dataSharingLabel.grid(row=4, column=3, sticky=W)

    dataSharingLabel1 = tk.Label(root, text="III.1 Data sharing strategy", font="Helvetica 10")
    dataSharingLabel1.grid(row=5, column=3, sticky=W)
    dataSharingText1 = tk.Text(root, width=70, height=5)
    dataSharingText1.insert(END,
                            "How and when will the data be shared and made accessible? What repository will you be using? What persistent identifier will be used?")
    dataSharingText1.grid(row=5, column=4, columnspan=2, sticky=W)

    dataSharingLabel2 = tk.Label(root, text="III.2 Data storage strategy", font="Helvetica 10")
    dataSharingLabel2.grid(row=6, column=3, sticky=W)
    dataSharingText2 = tk.Text(root, width=70, height=5)
    dataSharingText2.insert(END,
                            "What data are to be preserved for the long-term, and what data will not be stored? How and where will the data be stored and backed up during the research? How and where will the data be stored after the project ends? For how long will the data be stored? Are there any costs that need to be covered for storage? At what point during or after the project will the data be stored? Are there any technical barriers to making the research data fully or partially accessible?")
    dataSharingText2.grid(row=6, column=4, columnspan=2, sticky=W)

    ethicalLabel = tk.Label(root, text="IV Legal and Ethical Aspects", font="Helvetica 10")
    ethicalLabel.grid(row=7, column=3, sticky=W)

    ethicalLabel1 = tk.Label(root, text="IV.1 Legal aspects", font="Helvetica 10")
    ethicalLabel1.grid(row=8, column=3, sticky=W)
    ethicalText1 = tk.Text(root, width=70, height=5)
    ethicalText1.insert(END,
                        "Are there any legal barriers to making the research data fully or partially accessible? Who owns the data? What licence for reuse are you planning to attach to the data? Are there any restrictions on the re-use of the data? If so, why?")
    ethicalText1.grid(row=8, column=4, columnspan=2, sticky=W)

    ethicalLabel2 = tk.Label(root, text="IV.2 Ethical aspects", font="Helvetica 10")
    ethicalLabel2.grid(row=9, column=3, sticky=W)
    ethicalText2 = tk.Text(root, width=70, height=5)
    ethicalText2.insert(END,
                        "Are there any ethical barriers to making the research data fully or partially accessible? If applicable, how are you planning to deal with sensitive data during and after the project? Consider Ethics for researchers published by the European Commission or The European Code of Conduct for Research Integrity")
    ethicalText2.grid(row=9, column=4, columnspan=3, sticky=W)

    generatedDataLabel = tk.Label(root, text="No data will be generated\nor analysed", font="Helvetica 10")
    generatedDataLabel.grid(row=10, column=3, sticky=W)
    generatedDataText = tk.Text(root, width=70, height=5)
    generatedDataText.insert(END,
                             "The FWF recognises that some projects will not generate or analyse research data and similar materials. In these cases, a short explanation is required.")
    generatedDataText.grid(row=10, column=4, columnspan=3, sticky=W)


#############################
# Additional Functions

# TODO all things needed for filling in DMP

def create_html(template, output):
    """
    Creates an HTML file with given template and content.
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

    if template == "FWF":
        outputText = real_template.render(data_officer=dataOfficerText.get(1.0,END),
                                          data_characteristics=dataDescriptionText1.get(1.0,END),
                                          meta_standards=docMetaText1.get(1.0,END),
                                          data_documentation=docMetaText2.get(1.0,END),
                                          data_quality=docMetaText3.get(1.0,END),
                                          data_sharing=dataSharingText1.get(1.0,END),
                                          data_storage=dataSharingText2.get(1.0,END),
                                          legal=ethicalText1.get(1.0,END),
                                          generation=generatedDataText.get(1.0,END))
    else:
        # TODO think about how to extend DMP with title!
        outputText = real_template.render(abstract=abstractText.get(1.0,END),
                                          data_summary=dataDescriptionText1.get(1.0,END),
                                          fair_findable=fairText1.get(1.0,END),
                                          fair_accessible=fairText2.get(1.0,END),
                                          fair_interoperable=fairText3.get(1.0,END),
                                          fair_reuse=fairText4.get(1.0,END),
                                          resource=resourceText.get(1.0,END),
                                          security=securityText.get(1.0,END),
                                          ethical=ethicalText.get(1.0,END),
                                          other=otherText.get(1.0,END))

    html_file = open(output + ".html", "w")
    html_file.write(outputText)
    html_file.close()

    return output + ".html"


def create_pdf(html):
    """
    Converts a given HTML file into a PDF.
    :param html: HTML file
    :return: name of the resulting pdf file
    """

    # Define options
    pdf_options = {
        "page-size": "A4",
        "orientation": "portrait"
    }
    # TODO more things depending on template
    if selectedTemplate == "FWF":
        pdf_options["orientation"] = "landscape"


    # TODO: we will change this path, or use an other library for converting PDF!
    # TODO: otherwise just say that wkhtmltopdf needs to be pre-installed (and how) and added to windows path
    path_wkthmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    pdfkit.from_file(html, html.replace(".html", ".pdf"), configuration=config, options=pdf_options)
    return html.replace(".html", ".pdf")



#############################
# Open maDMP

fileLabel = tk.Label(root, text="maDMP File:", font="Helvetica 10")
fileLabel.grid(row=1, column=0, sticky = W)

fileEntry = tk.Entry(root, width = 40)
fileEntry.grid(row=1, column=1, sticky = W)

fileButton = tk.Button(root, text='Open maDMP', command=chooseMaDMP, width = 30)
fileButton.grid(row=1, column=2, columnspan = 2, sticky = W)

#############################
# Choose template

templateLabel = tk.Label(root, text="Template:", font="Helvetica 10")
templateLabel.grid(row=2, column=0, sticky = W)

templatesCombo = ttk.Combobox(root,  state="readonly",
                              values=["Horizon", "FWF"],  width = 38)
templatesCombo.grid(row = 2, column = 1, sticky = W)
templatesCombo.current(0)

templateButton = tk.Button(root, text='Choose Template', command=chooseTemplate, width = 30)
templateButton.grid(row=2, column=2, columnspan = 2, sticky = W)


root.mainloop()