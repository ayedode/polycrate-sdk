from typing import Literal

ApiV1HostsCreateRoleErrorComponentAttr = Literal["role"]

API_V1_HOSTS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_hosts_create_role_error_component_attr(value: str) -> ApiV1HostsCreateRoleErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
