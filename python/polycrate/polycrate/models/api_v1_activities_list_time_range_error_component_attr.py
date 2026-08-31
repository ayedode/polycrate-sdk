from typing import Literal

ApiV1ActivitiesListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_ACTIVITIES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActivitiesListTimeRangeErrorComponentAttr] = {
    "time_range",
}


def check_api_v1_activities_list_time_range_error_component_attr(
    value: str,
) -> ApiV1ActivitiesListTimeRangeErrorComponentAttr:
    if value in API_V1_ACTIVITIES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
