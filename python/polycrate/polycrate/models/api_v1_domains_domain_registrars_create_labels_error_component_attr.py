from typing import Literal

ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_domains_domain_registrars_create_labels_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
