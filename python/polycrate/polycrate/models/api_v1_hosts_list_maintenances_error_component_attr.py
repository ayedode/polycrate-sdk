from typing import Literal

ApiV1HostsListMaintenancesErrorComponentAttr = Literal["maintenances"]

API_V1_HOSTS_LIST_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListMaintenancesErrorComponentAttr] = {
    "maintenances",
}


def check_api_v1_hosts_list_maintenances_error_component_attr(
    value: str,
) -> ApiV1HostsListMaintenancesErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
