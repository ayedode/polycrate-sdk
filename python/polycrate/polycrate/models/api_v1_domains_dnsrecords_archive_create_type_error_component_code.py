from typing import Literal

ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_domains_dnsrecords_archive_create_type_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
