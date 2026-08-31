from typing import Literal

ApiV1HostsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_HOSTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_hosts_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1HostsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
