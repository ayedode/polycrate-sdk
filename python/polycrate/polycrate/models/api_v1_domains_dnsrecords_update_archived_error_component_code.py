from typing import Literal

ApiV1DomainsDnsrecordsUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnsrecords_update_archived_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateArchivedErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
