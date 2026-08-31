from typing import Literal

ApiV1DomainsDomainRegistrarsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_domain_registrars_create_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
