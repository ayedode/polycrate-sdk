from typing import Literal

ApiV1ContactgroupsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_CONTACTGROUPS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_contactgroups_list_time_range_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsListTimeRangeErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
