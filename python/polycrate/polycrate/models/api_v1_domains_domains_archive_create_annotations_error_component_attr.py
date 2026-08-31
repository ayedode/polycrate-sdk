from typing import Literal

ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_domains_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
