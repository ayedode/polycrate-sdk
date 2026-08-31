from typing import Literal

ApiV1DomainsDnszonesImportRecordsCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesImportRecordsCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_domains_dnszones_import_records_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesImportRecordsCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
