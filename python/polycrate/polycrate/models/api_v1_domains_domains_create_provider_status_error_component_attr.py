from typing import Literal

ApiV1DomainsDomainsCreateProviderStatusErrorComponentAttr = Literal["provider_status"]

API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateProviderStatusErrorComponentAttr
] = {
    "provider_status",
}


def check_api_v1_domains_domains_create_provider_status_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateProviderStatusErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_PROVIDER_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
