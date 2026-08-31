from typing import Literal

ApiV1HostsPartialUpdateProviderLocationErrorComponentAttr = Literal["provider_location"]

API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateProviderLocationErrorComponentAttr
] = {
    "provider_location",
}


def check_api_v1_hosts_partial_update_provider_location_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateProviderLocationErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PROVIDER_LOCATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
