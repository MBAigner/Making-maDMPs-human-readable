# Translation Scheme for the FWF Template

What kinds of data/source code will be generated or reused (type, format, volume)?
* Used attributes:	
    * dataset/type
    * dataset/distribution/format
    * dataset/distribution/bytesize
*	Reused data? This question cannot be answered from the maDMP

How will the research data be generated and which methods will be used? 
*	Used attributes: dataset/description

How will you structure the data and handle versioning? 
*	Used attributes: dataset/host/support_versioning

Who is the target audience?
*	Could not be answered

What metadata standards (if any) will be in use and why? (see Digital Curation Centre)
*	Used attributes:
    * dataset/metadata_id/metadata_id
    * dataset/metadata_id/metadata_id_type
*	Why they are used is not explained by the RDA Standard.

What information is needed for the data to be findable, accessible, interoperable and re-usable (FAIR) in the future? 

We include the following information for the according characteristics:
*	**Accessible**:
    *	If IDs are used in the maDMP, we use values like dataset/dataset_id
    *	dataset/distribution/host/certified_with  (information about certificates of repository)
    *	dataset/distribution/host/description (which respository was used)
    *	pid_system (if used!)
*	**Findable**:
    *	Dataset/keyword -> keywords usable for search
*	**Re-usable**:
    *	dataset/licence/license_ref (which licence was used for reusability)
    *	Metadata used (see above: dataset/metdata/metadata_id/metadata_id, dataset/metdata/metadata_id/metadata_id_type)
    *	metdata/language
    * dataset/language
    *	dataset/data_quality_assurance (e.g. naming conventions)
    *	distribution/host/backup_frequency
    * distribution/host/backup_type

Is the data machine-readable? 
*	**Interoperable**
   * We look if dataset/distribution/format is machine readable

How are you planning to document this information?
*	This is not answered by the madDMP

What quality assurance processes will you adopt? 
*	dataset/data_quality_assurance (e.g. naming conventions)

How will the consistency and quality of data collection be controlled and documented? (This may include processes such as repeat samples or measurements, standardised data capture, peer review of data or representation with controlled vocabularies.)
*	Not explained in JSON!

How and when will the data be shared and made accessible? 
* Used attributes:
   *	dataset/Distribution/access_url
   *	dataset/Distribution/available_till
   *	dataset/Distribution/data_access
   *	dataset/Distribution/download_url
   *	dataset/Distribution/license/licence_ref
   *	dataset/Distribution/license/start_date
   *	dataset/issued


What repository will you be using? 
* Used attributes:
   *	dataset/host/description
   *	dataset/host/geo_location
   *	dataset/host/pid_system

What persistent identifier will be used?
*	dataset/dataset_id/dataset_id
*	dataset/dataset_id/dataset_id_type

What data are to be preserved for the long-term, and what data will not be stored? 
*	dataset/preservation_statement

How and where will the data be stored and backed up during the research? 
*	dataset/host/geo_location

How and where will the data be stored after the project ends? 
*	dataset/preservation_statement

For how long will the data be stored? 
*	dataset/distribution/available_till

Are there any costs that need to be covered for storage? 
*	dataset/cost/*

At what point during or after the project will the data be stored?
* Used attributes:
   *	dataset/host/ backup_frequency
   *	dataset/host/ backup_type
*	not answered completely by the maDMP

Are there any technical barriers to making the research data fully or partially accessible?
*	Not answered by the maDMP

Are there any legal barriers to making the research data fully or partially accessible? 
* Who owns the data? 
   *	dataset/distribution/licence

What licence for reuse are you planning to attach to the data? 
*	dataset/distribution/licence

Are there any restrictions on the re-use of the data? If so, why?
* Used attributes:
   *	dataset/distribution/licence
   *	dataset/security_and_privacy
*	Why is not explained by the maDMP

Are there any ethical barriers to making the research data fully or partially accessible? 
*	ethical_issues_exist
*  ethical_issues_description
*  ethical_issues_report
*  dataset/personal_data

If applicable, how are you planning to deal with sensitive data during and after the project? 
* Used attributes:
   * dataset/sensitive_data
*	See ethical_issues_report, before and after the project is not explicitly defined for dataset/sensitive_data

No data will be generated or analysed
*	Not answered by the maDMP


