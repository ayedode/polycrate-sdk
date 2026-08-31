from typing import Literal

ApiV1ActivitiesListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_ACTIVITIES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActivitiesListTimeRangeErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_activities_list_time_range_error_component_code(
    value: str,
) -> ApiV1ActivitiesListTimeRangeErrorComponentCode:
    if value in API_V1_ACTIVITIES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
