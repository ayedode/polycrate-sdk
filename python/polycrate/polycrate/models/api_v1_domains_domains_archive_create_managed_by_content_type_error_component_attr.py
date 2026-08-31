from typing import Literal

ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponentAttr = Literal["managed_by_content_type"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponentAttr
] = {
    "managed_by_content_type",
}


def check_api_v1_domains_domains_archive_create_managed_by_content_type_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
