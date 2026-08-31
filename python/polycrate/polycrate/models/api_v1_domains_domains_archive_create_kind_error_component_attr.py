from typing import Literal

ApiV1DomainsDomainsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_domains_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
