from typing import Literal

ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_domain_registrars_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
