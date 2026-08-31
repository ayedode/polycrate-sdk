from typing import Literal

ApiV1HostsDiscoverCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_hosts_discover_create_provider_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateProviderErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
