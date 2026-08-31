from typing import Literal

ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_domains_dnszones_archive_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateArchivedByErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
