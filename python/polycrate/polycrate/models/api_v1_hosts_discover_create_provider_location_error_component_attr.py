from typing import Literal

ApiV1HostsDiscoverCreateProviderLocationErrorComponentAttr = Literal["provider_location"]

API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateProviderLocationErrorComponentAttr
] = {
    "provider_location",
}


def check_api_v1_hosts_discover_create_provider_location_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateProviderLocationErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
