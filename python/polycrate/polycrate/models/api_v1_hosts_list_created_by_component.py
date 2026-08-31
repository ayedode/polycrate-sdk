from typing import Literal

ApiV1HostsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_HOSTS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1HostsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_hosts_list_created_by_component(value: str) -> ApiV1HostsListCreatedByComponent:
    if value in API_V1_HOSTS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_CREATED_BY_COMPONENT_VALUES!r}")
