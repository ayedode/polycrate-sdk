from typing import Literal

ApiV1DomainsDomainsArchiveCreateNameserversErrorComponentAttr = Literal["nameservers"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_NAMESERVERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateNameserversErrorComponentAttr
] = {
    "nameservers",
}


def check_api_v1_domains_domains_archive_create_nameservers_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateNameserversErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_NAMESERVERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_NAMESERVERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
