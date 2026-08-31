from typing import Literal

ApiV1HostsListRoleErrorComponentAttr = Literal["role"]

API_V1_HOSTS_LIST_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_hosts_list_role_error_component_attr(value: str) -> ApiV1HostsListRoleErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
