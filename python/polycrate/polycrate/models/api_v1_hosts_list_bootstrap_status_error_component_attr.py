from typing import Literal

ApiV1HostsListBootstrapStatusErrorComponentAttr = Literal["bootstrap_status"]

API_V1_HOSTS_LIST_BOOTSTRAP_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListBootstrapStatusErrorComponentAttr] = {
    "bootstrap_status",
}


def check_api_v1_hosts_list_bootstrap_status_error_component_attr(
    value: str,
) -> ApiV1HostsListBootstrapStatusErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_BOOTSTRAP_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_BOOTSTRAP_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
