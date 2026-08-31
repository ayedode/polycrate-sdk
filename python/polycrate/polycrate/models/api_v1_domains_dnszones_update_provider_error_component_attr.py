from typing import Literal

ApiV1DomainsDnszonesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_DOMAINS_DNSZONES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_domains_dnszones_update_provider_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateProviderErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
