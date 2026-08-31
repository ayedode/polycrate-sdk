from typing import Literal

ApiV1DomainsDnszonesImportRecordsCreateZoneTextErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_ZONE_TEXT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesImportRecordsCreateZoneTextErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_domains_dnszones_import_records_create_zone_text_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesImportRecordsCreateZoneTextErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_ZONE_TEXT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_ZONE_TEXT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
