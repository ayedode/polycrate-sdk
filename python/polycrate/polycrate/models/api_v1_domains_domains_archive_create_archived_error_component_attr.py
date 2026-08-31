from typing import Literal

ApiV1DomainsDomainsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_domains_domains_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
