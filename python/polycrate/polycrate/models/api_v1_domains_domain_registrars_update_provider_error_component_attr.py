from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_domains_domain_registrars_update_provider_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateProviderErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
