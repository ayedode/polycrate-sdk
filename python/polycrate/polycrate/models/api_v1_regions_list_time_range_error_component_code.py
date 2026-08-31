from typing import Literal

ApiV1RegionsListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_REGIONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsListTimeRangeErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_regions_list_time_range_error_component_code(
    value: str,
) -> ApiV1RegionsListTimeRangeErrorComponentCode:
    if value in API_V1_REGIONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
