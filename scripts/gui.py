import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

DEBUG = True

root = tk.Tk()
root.title("Making-maDMPs-human-readablse")
root.style = Style()
root.style.theme_use("clam")
#('clam', 'alt', 'default', 'classic')

title = tk.Label(root, text="Making-maDMPs-human-readable",
                 font="Helvetica 16 bold")
title.grid(row = 0, columnspan=6, sticky = N)

#############################
# GUI Functions

def chooseMaDMP(event=None):
    """
    Upload dialog for maDMPs
    """
    file_name = filedialog.askopenfilename()
    if DEBUG:
        print('Selected:', file_name)
    fileEntry.insert(0, file_name)


def chooseTemplate(event=None):
    """
    Upload dialog for maDMPs
    """
    if templatesCombo.get() == "FWF": # load FWF template
        dataOfficerText, dataDescriptionText1, docMetaText1, docMetaText2, docMetaText3, \
        ethicalText1, ethicalText2, generatedDataText = createFWFItems()
    else: # load Horizon template
        pass # TODO


def createHorizonItems():
    pass # TODO


def createFWFItems():
    """
    Fills in all GUI items necessary for FWF template
    """
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
    ethicalText2.grid(row=9, column=1, columnspan=3, sticky=W)

    generatedDataLabel = tk.Label(root, text="No data will be generated or analysed", font="Helvetica 10")
    generatedDataLabel.grid(row=9, column=3, sticky=W)
    generatedDataText = tk.Text(root, width=70, height=5)
    generatedDataText.insert(END,
                             "The FWF recognises that some projects will not generate or analyse research data and similar materials. In these cases, a short explanation is required.")
    generatedDataText.grid(row=9, column=4, columnspan=3, sticky=W)

    return dataOfficerText, dataDescriptionText1, docMetaText1, docMetaText2, docMetaText3, \
           ethicalText1, ethicalText2, generatedDataText


#############################
# Open maDMP

fileLabel = tk.Label(root, text="maDMP File:", font="Helvetica 10")
fileLabel.grid(row=1, column=0, sticky = W)

fileEntry = tk.Entry(root, width = 40)
fileEntry.grid(row=1, column=1, sticky = W)

fileButton = tk.Button(root, text='Open maDMP', command=chooseMaDMP)
fileButton.grid(row=1, column=2, sticky = W)

#############################
# Choose template

templateLabel = tk.Label(root, text="Template:", font="Helvetica 10")
templateLabel.grid(row=2, column=0, sticky = W)

templatesCombo = ttk.Combobox(root,  state="readonly",
                              values=["Horizon", "FWF"])
templatesCombo.grid(row = 2, column = 1, sticky = W)
templatesCombo.current(0)

templateButton = tk.Button(root, text='Choose Template', command=chooseTemplate)
templateButton.grid(row=2, column=2, sticky = W)

#############################
# Modify DMP text

button1 = tk.Button(root, text='Fill in DMP data', command=chooseMaDMP) # TODO
button1.grid(row=3, column=0, sticky = W)

button2 = tk.Button(root, text='Reset DMP data', command=chooseMaDMP)
button2.grid(row=3, column=1, sticky = W)

#############################
# FWF template

# dataOfficerLabel = tk.Label(root, text="Data Officer", font="Helvetica 10")
# dataOfficerLabel.grid(row=4, column=0, sticky = W)
# dataOfficerText = tk.Text(root, width = 70, height = 5)
# dataOfficerText.insert(END, "Who is responsible for the data management and "
#                             "the DMP of the project (name/email address)?")
# dataOfficerText.grid(row=4, column=1, columnspan = 2, sticky = W)
#
# dataDescriptionLabel = tk.Label(root, text="I Data Characteristics", font="Helvetica 10")
# dataDescriptionLabel.grid(row=5, column=0, sticky = W)
#
# dataDescriptionLabel1 = tk.Label(root, text="I.1 Description of the data", font="Helvetica 10")
# dataDescriptionLabel1.grid(row=6, column=0, sticky = W)
# dataDescriptionText1 = tk.Text(root, width = 70, height = 5)
# dataDescriptionText1.insert(END, "What kinds of data/source code will be generated or reused (type, format, volume)? "
#                                   "How will the research data be generated and which methods will be used? "
#                                   "How will you structure the data and handle versioning? Who is the target audience?")
# dataDescriptionText1.grid(row=6, column=1, columnspan = 2, sticky = W)
#
#
# docMetaLabel = tk.Label(root, text="II Documentation and Metadata", font="Helvetica 10")
# docMetaLabel.grid(row=7, column=0, sticky = W)
#
# docMetaLabel1 = tk.Label(root, text="II.1 Metadata standards", font="Helvetica 10")
# docMetaLabel1.grid(row=8, column=0, sticky = W)
# docMetaText1 = tk.Text(root, width = 70, height = 5)
# docMetaText1.insert(END, "What metadata standards (if any) will be in use and why? (see Digital Curation Centre)")
# docMetaText1.grid(row=8, column=1, columnspan = 2, sticky = W)
#
# docMetaLabel2 = tk.Label(root, text="II.2 Documentation of data", font="Helvetica 10")
# docMetaLabel2.grid(row=9, column=0, sticky = W)
# docMetaText2 = tk.Text(root, width = 70, height = 5)
# docMetaText2.insert(END, "What information is needed for the data to be findable, accessible, interoperable and re-usable (FAIR) in the future? Is the data machine-readable? How are you planning to document this information?")
# docMetaText2.grid(row=9, column=1, columnspan = 2, sticky = W)
#
# docMetaLabel3 = tk.Label(root, text="II.3 Data quality control", font="Helvetica 10")
# docMetaLabel3.grid(row=10, column=0, sticky = W)
# docMetaText3 = tk.Text(root, width = 70, height = 5)
# docMetaText3.insert(END, "What quality assurance processes will you adopt? How will the consistency and quality of data collection be controlled and documented? (This may include processes such as repeat samples or measurements, standardised data capture, peer review of data or representation with controlled vocabularies.")
# docMetaText3.grid(row=10, column=1, columnspan = 2, sticky = W)
#
# dataSharingLabel = tk.Label(root, text="III Data Availability and Storage", font="Helvetica 10")
# dataSharingLabel.grid(row=4, column=3, sticky = W)
#
# dataSharingLabel1 = tk.Label(root, text="III.1 Data sharing strategy", font="Helvetica 10")
# dataSharingLabel1.grid(row=5, column=3, sticky = W)
# dataSharingText1 = tk.Text(root, width = 70, height = 5)
# dataSharingText1.insert(END, "How and when will the data be shared and made accessible? What repository will you be using? What persistent identifier will be used?")
# dataSharingText1.grid(row=5, column=4, columnspan = 2, sticky = W)
#
# dataSharingLabel2 = tk.Label(root, text="III.2 Data storage strategy", font="Helvetica 10")
# dataSharingLabel2.grid(row=6, column=3, sticky = W)
# dataSharingText2 = tk.Text(root, width = 70, height = 5)
# dataSharingText2.insert(END, "What data are to be preserved for the long-term, and what data will not be stored? How and where will the data be stored and backed up during the research? How and where will the data be stored after the project ends? For how long will the data be stored? Are there any costs that need to be covered for storage? At what point during or after the project will the data be stored? Are there any technical barriers to making the research data fully or partially accessible?")
# dataSharingText2.grid(row=6, column=4, columnspan = 2, sticky = W)
#
#
# ethicalLabel = tk.Label(root, text="IV Legal and Ethical Aspects", font="Helvetica 10")
# ethicalLabel.grid(row=7, column=3, sticky = W)
#
# ethicalLabel1 = tk.Label(root, text="IV.1 Legal aspects", font="Helvetica 10")
# ethicalLabel1.grid(row=8, column=3, sticky = W)
# ethicalText1 = tk.Text(root, width = 70, height = 5)
# ethicalText1.insert(END, "Are there any legal barriers to making the research data fully or partially accessible? Who owns the data? What licence for reuse are you planning to attach to the data? Are there any restrictions on the re-use of the data? If so, why?")
# ethicalText1.grid(row=8, column=4, columnspan = 2, sticky = W)
#
# ethicalLabel2 = tk.Label(root, text="IV.2 Ethical aspects", font="Helvetica 10")
# ethicalLabel2.grid(row=9, column=3, sticky = W)
# ethicalText2 = tk.Text(root, width = 70, height = 5)
# ethicalText2.insert(END, "Are there any ethical barriers to making the research data fully or partially accessible? If applicable, how are you planning to deal with sensitive data during and after the project? Consider Ethics for researchers published by the European Commission or The European Code of Conduct for Research Integrity")
# ethicalText2.grid(row=9, column=1, columnspan = 3, sticky = W)
#
# generatedDataLabel = tk.Label(root, text="No data will be generated or analysed", font="Helvetica 10")
# generatedDataLabel.grid(row=9, column=3, sticky = W)
# generatedDataText = tk.Text(root, width = 70, height = 5)
# generatedDataText.insert(END, "The FWF recognises that some projects will not generate or analyse research data and similar materials. In these cases, a short explanation is required.")
# generatedDataText.grid(row=9, column=4, columnspan = 3, sticky = W)


#############################
# Save result

button = tk.Button(root, text='Save DMP', command=chooseMaDMP)
button.grid(row=11, column=0, columnspan = 6, sticky = S)

root.mainloop()
