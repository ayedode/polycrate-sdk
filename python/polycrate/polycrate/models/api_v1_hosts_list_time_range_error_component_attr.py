from typing import Literal

ApiV1HostsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_HOSTS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsListTimeRangeErrorComponentAttr] = {
    "time_range",
}


def check_api_v1_hosts_list_time_range_error_component_attr(value: str) -> ApiV1HostsListTimeRangeErrorComponentAttr:
    if value in API_V1_HOSTS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
