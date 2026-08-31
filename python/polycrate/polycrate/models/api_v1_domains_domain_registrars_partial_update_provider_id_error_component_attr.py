from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_domains_domain_registrars_partial_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateProviderIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
