from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_domain_registrars_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
