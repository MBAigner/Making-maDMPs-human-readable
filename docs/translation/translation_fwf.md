# Translation Scheme for the FWF Template

What kinds of data/source code will be generated or reused (type, format, volume)?
*	Dataset/type + dataset/distribution/format + dataset/distribution/bytesize
*	Reused? Cannot be answered from maDMP

How will the research data be generated and which methods will be used? 
*	Dataset/description

How will you structure the data and handle versioning? 
*	Dataset/host/support_versioning

Who is the target audience?
*	Could not be answered

What metadata standards (if any) will be in use and why? (see Digital Curation Centre)
*	Dataset/metadata_id/metadata_id + Dataset/metadata_id/metadata_id_type
*	Why not explained

What information is needed for the data to be findable, accessible, interoperable and re-usable (FAIR) in the future? 
*	Accessible:
    *	If they use ids -> e.g. dataset/dataset_id
    *	Dataset/Distribution/Host/certified_with  (certificates of repository)
    *	Dataset /Distribution/Host/description -> which repo was used
    *	pid_system (if used!)
*	findable:
    *	Dataset/keyword -> keywords usable for search
*	re-usable:
    *	dataset/licence/license_ref -> which licence was used for reusability
    *	Metadata used -> see above (Dataset/ metdata/metadata_id/metadata_id + Dataset/ metdata/metadata_id/metadata_id_type)
    *	Metdata/language + dataset/language
    *	Dataset/data_quality_assurance (e.g. naming conventions)
    *	distribution/host/backup_frequency + distribution/host/backup_type +

Is the data machine-readable? 
*	interoperable: See if dataset/distribution/format is machine readable (in principle -> csv could still be bad -> thus let user change stuff in editor!)

How are you planning to document this information?
*	Not answered imo by json file

•	What quality assurance processes will you adopt? 
*	Dataset/data_quality_assurance (e.g. naming conventions)

How will the consistency and quality of data collection be controlled and documented? (This may include processes such as repeat samples or measurements, standardised data capture, peer review of data or representation with controlled vocabularies.)
*	Not explained in JSON!

How and when will the data be shared and made accessible? 

*	Dataset/Distribution/access_url
*	Dataset/Distribution/available_till
*	Dataset/Distribution/data_access
*	Dataset/Distribution/download_url
*	Dataset/Distribution/license/licence_ref
*	Dataset/Distribution/license/start_date
*	Dataset/issued


What repository will you be using? 
*	Dataset/host/description
*	Dataset/host/geo_location
*	Dataset/host/pid_system

What persistent identifier will be used?
*	Dataset/dataset_id/dataset_id
*	Dataset/dataset_id/dataset_id_type

What data are to be preserved for the long-term, and what data will not be stored? 
*	Dataset/preservation_statement

How and where will the data be stored and backed up during the research? 
*	Dataset/host/geo_location

How and where will the data be stored after the project ends? 
*	Dataset/preservation_statement

For how long will the data be stored? 
*	Dataset/distribution/available_till

Are there any costs that need to be covered for storage? 
*	Dataset/cost/*

At what point during or after the project will the data be stored? 
*	Dataset/host/ backup_frequency
*	Dataset/host/ backup_type
*	Not answered by the maDMP completely

Are there any technical barriers to making the research data fully or partially accessible?
*	Not answered by the maDMP

•	Are there any legal barriers to making the research data fully or partially accessible? 

Who owns the data? 
*	Dataset/distribution/licence

What licence for reuse are you planning to attach to the data? 
*	Dataset/distribution/licence

Are there any restrictions on the re-use of the data? If so, why?
*	Dataset/distribution/licence
*	Why is not explained by maDmp
*	Dataset/Security_and_privacy

Are there any ethical barriers to making the research data fully or partially accessible? 
*	ethical_issues_exist, ethical_issues_description, ethical_issues_report, dataset/personal_data

If applicable, how are you planning to deal with sensitive data during and after the project? 
*	See ethical_issues_report, dataset/sensitive_data -> before and after the project is not explicitly defined

No data will be generated or analysed
*	Not answered by the maDMP


