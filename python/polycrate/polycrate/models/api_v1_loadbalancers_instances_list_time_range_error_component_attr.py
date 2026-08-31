from typing import Literal

ApiV1LoadbalancersInstancesListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_LOADBALANCERS_INSTANCES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_loadbalancers_instances_list_time_range_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListTimeRangeErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
