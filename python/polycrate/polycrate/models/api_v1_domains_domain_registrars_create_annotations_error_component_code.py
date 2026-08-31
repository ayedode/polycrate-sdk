from typing import Literal

ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domain_registrars_create_annotations_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateAnnotationsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
