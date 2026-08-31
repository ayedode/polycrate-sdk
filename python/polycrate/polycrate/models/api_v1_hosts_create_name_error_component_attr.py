from typing import Literal

ApiV1HostsCreateNameErrorComponentAttr = Literal["name"]

API_V1_HOSTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_hosts_create_name_error_component_attr(value: str) -> ApiV1HostsCreateNameErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
