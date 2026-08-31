from typing import Literal

ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_domains_dnszones_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
