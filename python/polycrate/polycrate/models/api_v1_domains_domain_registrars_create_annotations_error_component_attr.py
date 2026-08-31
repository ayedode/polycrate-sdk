from typing import Literal

ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_domain_registrars_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
