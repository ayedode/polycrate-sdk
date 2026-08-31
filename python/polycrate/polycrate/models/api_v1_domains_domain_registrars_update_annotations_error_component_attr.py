from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_domain_registrars_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
