from typing import Literal

ApiV1HostsUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_HOSTS_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateHostnameErrorComponentAttr] = {
    "hostname",
}


def check_api_v1_hosts_update_hostname_error_component_attr(value: str) -> ApiV1HostsUpdateHostnameErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
