from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_domain_registrars_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
