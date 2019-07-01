# Comparison of original DMPs with the generated DMPs


### a. How do they differ?

In general, we observed that some information of the original DMPs got lost through the conversion into an maDMP and again into a hrDMP.

This was due some missing fields of the RDA standard containing relevant information for each subquestion contained in the templates, resulting in a marginal loss of information.

However, the look and feel of the content of the created DMPs is similar to the ones written by hand. 

There are still some differences regarding the style of the resulting hrDMPs, mostly for the FWF template.


## b. What information got lost?

We want to divide our comparison of the differences of the orginal DMPs and our translated ones into two sections, one for each template - Horizon 2020 and FWF - we treated in our work.

Here we want to give an overview about the lost information. More detailed descriptions are included under the GitHub Pages for our [Translation Scheme](https://github.com/MBAigner/Making-maDMPs-human-readable/blob/master/docs/translation/translation.md), regarding included and missing attributes.

### b.1. FWF

We have not been able to include the information of our original DMP for the following questions/sections:

* What kinds of data/source code will be generated or reused (type, format, volume)? The information which data was reused could not be reassembled with the maDMP.
* How are you planning to document this information?
* How will the consistency and quality of data collection be controlled and documented?
* Are there any technical barriers to making the research data fully or partially accessible?
* If applicable, how are you planning to deal with sensitive data during and after the project? Before and after the project is not specified
* No data will be generated or analysed. This is not answered by the maDMP.
    *  For this section, none of the needed information could be obtained from the JSON file.

### b.2. Horizon 2020

We have not been able to include the information of our original DMP for the following questions, respectively just sub-questions:

* Specify if existing data is being re-used (if any)?
* Outline the data utility: to whom will it be useful? 
* Specify what methods or software tools are needed to access the data? Is documentation about the software needed to access the data included? Is it possible to include the relevant software (e.g. in open source code)? 
* Specify whether you will be using standard vocabulary for all data types present in your data set, to allow inter-disciplinary interoperability? If not, will you provide mapping to more commonly used ontologies? 

For those questions, no information is provided in the maDMPs.

* Specify whether the data produced and/or used in the project is useable by third parties, in particular after the end of the project? If the re-use of some data is restricted, explain why? The information, except the third party use is specified in maDMP.
* Describe costs and potential value of long term preservation. The value of long term preservation was hard to find in the maDMP.
* Also, recovery and explicitly secure storage and transfer of data not defined in maDMP.


## c. Which information is more detailed?

In general, the loss of information was bigger through the conversion than the additional amount of more detailed information. However, due to the usage of the full, artificial maDMP, we included some information that was not contained in our original versions, like

* Cost of the project
* Technical devices used
* Some details about back-ups and availability
* Funding

## d. Which parts of the maDMP were easy/hard to generate?

Some parts of the template, like the Creator for Horizon 2020 or Data Officer for FWF have been easiest to extract from the maDMP. 

A big problem was the dataset attributes, because it contains a big amount of data, especially bigger arrays appearing in the JSON what made it a real challenge and a lot of work was necessary to fit the whole information into our human-readable DMPs.

For all other attributes of the maDMPs, the integration into our hrDMPs has been quite easy.


## Solutions regarding the problems of missing information

We implemented the possibility for a user of our tool to manually adjust the resulting human-readable DMP. 

Thus, formulations can be changed, and missing information can be still added by hand if it is either not appearing in the machine-actionable DMP, or hard to generate.
