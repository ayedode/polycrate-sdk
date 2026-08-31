from typing import Literal

ApiV1DomainsDomainsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_domains_domains_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
