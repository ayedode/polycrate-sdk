from typing import Literal

ApiV1DomainsDnszonesImportRecordsCreateZoneTextErrorComponentAttr = Literal["zone_text"]

API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_ZONE_TEXT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesImportRecordsCreateZoneTextErrorComponentAttr
] = {
    "zone_text",
}


def check_api_v1_domains_dnszones_import_records_create_zone_text_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesImportRecordsCreateZoneTextErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_ZONE_TEXT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_IMPORT_RECORDS_CREATE_ZONE_TEXT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
