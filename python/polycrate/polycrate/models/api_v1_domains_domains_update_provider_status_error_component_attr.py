from typing import Literal

ApiV1DomainsDomainsUpdateProviderStatusErrorComponentAttr = Literal["provider_status"]

API_V1_DOMAINS_DOMAINS_UPDATE_PROVIDER_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateProviderStatusErrorComponentAttr
] = {
    "provider_status",
}


def check_api_v1_domains_domains_update_provider_status_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateProviderStatusErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_PROVIDER_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_PROVIDER_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
