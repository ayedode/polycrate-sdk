from typing import Literal

ApiV1HostsPartialUpdateRoleErrorComponentAttr = Literal["role"]

API_V1_HOSTS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsPartialUpdateRoleErrorComponentAttr] = {
    "role",
}


def check_api_v1_hosts_partial_update_role_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateRoleErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_ROLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
