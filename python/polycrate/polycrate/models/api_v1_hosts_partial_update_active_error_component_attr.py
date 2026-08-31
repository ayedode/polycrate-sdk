from typing import Literal

ApiV1HostsPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_HOSTS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsPartialUpdateActiveErrorComponentAttr] = {
    "active",
}


def check_api_v1_hosts_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateActiveErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
