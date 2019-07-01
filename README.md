# Making maDMPs human-readable

## Overview

Machine-actionable DMPs help to present information in a structured way. However, some funders still require human-readable DMPs.

Thats why we developed our tool, making maDMPs human-readable, enabling an easy and user-friendly generation of human-readable DMPs out of maDMPs.

## Description of our Solution

For the purpose of transforming machine-actionable DMPs into human-readable ones, we implemented a GUI application. Using our tool, one can 

* upload a maDMP in form of a JSON file
* select one of two supported templates (FWF or Horizon 2020)
* let the tool automatically fill out fields for all questions provided in the templates
* adapt automatically generated translation for a better fit to the users needs
* save the resulting, human-readable DMP as HTML and/or PDF document

Some more detailed examples about how to use our tool can be found [here](https://github.com/MBAigner/Making-maDMPs-human-readable/blob/master/docs/examples/example.md).

The code implemented for our tool can be found under this site: [source code](https://github.com/MBAigner/Making-maDMPs-human-readable/tree/master/scripts).

## Folder Structure

*  ```templates```: Contains template files that will be feeded with maDMP data when executing our tool.
*  ```hrDMPs```: Here we saved some sample human-readable DMPs created with the tool.
*  ```maDMPs```: Contains our created maDMPs, used for the evaluation of our tool.
*  ```scripts```: This folder consists of all code needed for the execution of the tool.

## Instructions

The main file of our tool can be found in the directory  ```scripts```. In the following, we will show up needed software and libraries for the execution of our tool.

### Needed libraries and pre-installed software

* ```python``` version 3.6
* ```tkinter``` version 8.6
* ```jinja2``` version 2.10.1
* ```pdfkit``` version 0.6.1

Also, the software  ```wkhtmltopdf ``` needs to be installed, for the creation of pdf documents. Guides how to install this on a certain operating system can be found [here](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf/). We used version 0.12.4 for our project.

## How-to

We want to show some use-case how to use our tool for an effective translation of maDMPs into hrDMPs. Some examples can be found here: [How-To](https://github.com/MBAigner/Making-maDMPs-human-readable/blob/master/docs/examples/example.md).

## Original human-readable DMPs

Our original human-readable DMPs, used for the creation of the maDMPs, can be found [here](https://github.com/MBAigner/Making-maDMPs-human-readable/tree/master/original_hrDMPs).

## maDMP samples

The machine-actionable DMPs used for the evaluation of our tool can be used [here](https://github.com/MBAigner/Making-maDMPs-human-readable/tree/master/maDMPs).

## Parsing scheme

Here, we want to demonstrate the scheme we used for parsing the structured information of an maDMP into the necessary fields of an hrDMP, supporting the FWF and Horizon 2020 DMP templates.

Our used scheme can be found [here](https://github.com/MBAigner/Making-maDMPs-human-readable/blob/master/docs/translation/translation.md).

## hrDMP samples

The human-readable DMPs created with our tool can be found under [this](https://github.com/MBAigner/Making-maDMPs-human-readable/tree/master/hrDMPs) link.

## Comparison of DMPs

A detailed comparison between the created, human-readable DMPs and the original versions of them can be found [here](https://github.com/MBAigner/Making-maDMPs-human-readable/blob/master/docs/comparison/comparison.md).
