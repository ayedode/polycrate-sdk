from typing import Literal

ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_domains_domain_registrars_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateProviderIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
