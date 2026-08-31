from typing import Literal

ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponentAttr = Literal["type"]

API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponentAttr
] = {
    "type",
}


def check_api_v1_domains_dnsrecords_archive_create_type_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsArchiveCreateTypeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
