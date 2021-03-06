# Translation Scheme for the Horizon 2020 Template

**Abstract of the DMP**

* Title: dmp/title
* A Data Management Plan created using DMPonline 
* Creator: dmp/contact/name (dmp/contact/contact_id/contact_id)
* Affiliation: not given in maDMP
* Template: European Commission (Horizon 2020) 
* Last modified: -> dmp/modified

**Title of the DMP**
* dmp/title - Detailed DMP 

**1. Data summary**
* State the purpose of the data collection/generation 
    *	dmp/project
* Explain the relation to the objectives of the project 
    *	dmp/project
* Specify the types and formats of data generated/collected 
    *	dataset/type
    *	dmp/dataset/distribution/format
* Specify if existing data is being re-used (if any) 
    * not explicitly specified in the maDMP
* Specify the origin of the data 
    *	dataset/ description (otherwise not explicitly specified in the maDMP)
* State the expected size of the data (if known) 
    *	dataset/distribution/ byte_size
* Outline the data utility: to whom will it be useful 
    *	not specified explicitly in the maDMP

**2.1 Making data findable, including provisions for metadata [FAIR data]**
* Outline the discoverability of data (metadata provision) 
    * Metadata used metdata/metadata_id/metadata_id + Dataset/ metdata/metadata_id/metadata_id_type
    * metdata/language + metadata/description

* Outline the identifiability of data and refer to standard identification mechanism. Do you make use of persistent and unique identifiers such as Digital Object Identifiers?
  * contact/contact_id/contact_id_type
  * staff_id/staff_id_type
  * dmp_id/dmp_id_type
  * pid_system
  * meta_data/meta_data_id/meta_data_id_type
  * resource_id/technical_reosurce_id_type
  * funding/funder_id/funder_id_type
  * funding/grant_id/grant_id_type

* Outline naming conventions used 
    *	dataset/data_quality_assurance

* Outline the approach towards search keyword 
    *	dataset/keyword

* Outline the approach for clear versioning 
    *	dataset/host/support_versioning + dataset/host/description (other versioning techniques need to be filled out by hand)

* Specify standards for metadata creation (if any). If there are no standards in your discipline describe what metadata will be created and how 
     * dataset/metadata/*
     * especially dataset/metadata/metadata_id (e.g. Dublin core), dataset/metadata/language and dataset/metadata/description

**2.2 Making data openly accessible [FAIR data]**

* Specify which data will be made openly available? If some data is kept closed provide rationale for doing so 
  * dataset/preservation_statement
  * dataset/sensitive_data
  * dataset/personal_data
  * dataset/security_and_privacy
  
* Specify how the data will be made available 
  * dataset/distribution/access_url
  * dataset/distribution/download_url
  * dataset/distribution/available_till
  * dataset/distribution/license
  * dataset/distribution/format
  * dataset/distribution/host/description
  
* Specify what methods or software tools are needed to access the data? Is documentation about the software needed to access the data included? Is it possible to include the relevant software (e.g. in open source code)? 
  * No specified in maDMP

* Specify where the data and associated metadata, documentation and code are deposited
  * Used Attributes:
  * dataset/distribution/access_url
  * dataset/distribution/download_url
  * dataset/metadata/metadata_id
  * dataset/host/pid_system
  * Documentation not specified in maDMP

* Specify how access will be provided in case there are any restrictions 
    *	dataset/security_and_privacy
    * Access in that case is not specified explicitly

**2.3 Making data interoperable [FAIR data]**
* Assess the interoperability of your data. Specify what data and metadata vocabularies, standards or methodologies you will follow to facilitate interoperability. 
    *	dataset/metdata/metadata_id/metadata_id
    * dataset/metdata/metadata_id/metadata_id_type
    *	dataset/data_quality_assurance

* Specify whether you will be using standard vocabulary for all data types present in your data set, to allow inter-disciplinary interoperability? If not, will you provide mapping to more commonly used ontologies? 
    *	Not specified in maDMP

**2.4 Increase data re-use (through clarifying licenses) [FAIR data]**
* Specify how the data will be licenced to permit the widest reuse possible 
    * dataset/distribution/license/license_ref
    * dataset/distribution/license/start_date

* Specify when the data will be made available for re-use. If applicable, specify why and for what period a data embargo is needed 
    *	dataset/issued 
    *	dataset/distribution/license/start_date (embargo if date is in the future, however reason unknown)

* Specify whether the data produced and/or used in the project is useable by third parties, in particular after the end of the project?If the re-use of some data is restricted, explain why 
  *	dataset/distribution/licence
  *	dataset/Security_and_privacy
  *	Third party use is not specified in maDMP!
  *	Why is not explained by maDmp
  
* Describe data quality assurance processes 
    *	dataset/data_quality_assurance

* Specify the length of time for which the data will remain re-usable 
    *  dataset/distribution/available_till

**3. Allocation of resources**

* Estimate the costs for making your data FAIR. Describe how you intend to cover these costs 
  *	dataset/cost/currency_code 
  *	dataset/cost/description
  *	dataset/cost/title
  *	dataset/cost/value
  *	These describe the total cost. We have no separation between costs to make the data fair and long term preservation (see below)

* Clearly identify responsibilities for data management in your project 
  *	dm_staff/contributor_type (where contributer type is related to data management, e.g. data manager or all types)
  *	dm_staff/mbox
  *	dm_staff/name
  *	dm_staff/staff_id/staff_id
  *	dm_staff/staff_id/staff_id_type

* Describe costs and potential value of long term preservation 
    *	Costs: for long term preservation hard to find (e.g. title through "long term preservation"?), because this is not a general term for such costs found in every maDMP, we have not included this attribute.
    *	Value: dataset/distribution/preservation_statement

**4. Data security**
* Address data recovery as well as secure storage and transfer of sensitive data 
  *	dataset/sensitive_data
  *	dataset/security_and_privacy
  *	dataset/personal_data
  *	For sensitive data: dataset/distribution/host/description and dataset/distribution/data_access
  *	Recovery and explicitly secure storage and transfer of data not defined in maDMP

**5. Ethical aspects** 
* To be covered in the context of the ethics review, ethics section of DoA and ethics deliverables. Include references and related technical aspects if not covered by the former 
  *	ethical_issues_description
  *	ethical_issues_exist
  *	ethical_issues_report

**6. Other**
* Refer to other national/funder/sectorial/departmental procedures for data management that you are using (if any) 
  *	project
  *	funding
  *	funder_id
  *	funder_id
  *	funder_id_type
  *	funding_status
  *	grant_id
  *	grant_id
  *	grant_id_type
