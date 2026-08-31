from typing import Literal

ApiV1HostsPartialUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_HOSTS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_hosts_partial_update_hostname_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateHostnameErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
