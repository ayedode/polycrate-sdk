from typing import Literal

ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_dnsrecords_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
