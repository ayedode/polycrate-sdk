from typing import Literal

ApiV1HostsListNameErrorComponentAttr = Literal["name"]

API_V1_HOSTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_hosts_list_name_error_component_attr(value: str) -> ApiV1HostsListNameErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
