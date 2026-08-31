from typing import Literal

ApiV1HostsListHostnameErrorComponentAttr = Literal["hostname"]

API_V1_HOSTS_LIST_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListHostnameErrorComponentAttr] = {
    "hostname",
}


def check_api_v1_hosts_list_hostname_error_component_attr(value: str) -> ApiV1HostsListHostnameErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
