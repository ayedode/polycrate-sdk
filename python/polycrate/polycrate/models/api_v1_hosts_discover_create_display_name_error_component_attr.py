from typing import Literal

ApiV1HostsDiscoverCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_HOSTS_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_hosts_discover_create_display_name_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateDisplayNameErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
