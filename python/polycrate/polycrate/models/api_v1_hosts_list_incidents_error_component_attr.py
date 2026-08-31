from typing import Literal

ApiV1HostsListIncidentsErrorComponentAttr = Literal["incidents"]

API_V1_HOSTS_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListIncidentsErrorComponentAttr] = {
    "incidents",
}


def check_api_v1_hosts_list_incidents_error_component_attr(value: str) -> ApiV1HostsListIncidentsErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
