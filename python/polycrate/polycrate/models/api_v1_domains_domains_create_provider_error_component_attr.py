from typing import Literal

ApiV1DomainsDomainsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_domains_domains_create_provider_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateProviderErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
