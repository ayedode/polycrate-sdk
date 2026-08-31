from typing import Literal

ApiV1DomainsDnszonesImportRecordsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesImportRecordsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_import_records_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesImportRecordsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
