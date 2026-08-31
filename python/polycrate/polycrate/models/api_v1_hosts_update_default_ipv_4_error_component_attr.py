from typing import Literal

ApiV1HostsUpdateDefaultIpv4ErrorComponentAttr = Literal["default_ipv4"]

API_V1_HOSTS_UPDATE_DEFAULT_IPV_4_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateDefaultIpv4ErrorComponentAttr] = {
    "default_ipv4",
}


def check_api_v1_hosts_update_default_ipv_4_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateDefaultIpv4ErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_DEFAULT_IPV_4_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_DEFAULT_IPV_4_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
