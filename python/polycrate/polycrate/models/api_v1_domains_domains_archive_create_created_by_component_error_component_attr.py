from typing import Literal

ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_domains_domains_archive_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
