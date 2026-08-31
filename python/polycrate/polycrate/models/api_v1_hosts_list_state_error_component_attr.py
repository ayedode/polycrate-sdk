from typing import Literal

ApiV1HostsListStateErrorComponentAttr = Literal["state"]

API_V1_HOSTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_hosts_list_state_error_component_attr(value: str) -> ApiV1HostsListStateErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
