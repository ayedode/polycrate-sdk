from typing import Literal

ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domain_registrars_create_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
