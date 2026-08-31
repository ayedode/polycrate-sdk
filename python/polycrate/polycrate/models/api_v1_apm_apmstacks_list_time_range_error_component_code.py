from typing import Literal

ApiV1ApmApmstacksListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_APM_APMSTACKS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ApmApmstacksListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_apm_apmstacks_list_time_range_error_component_code(
    value: str,
) -> ApiV1ApmApmstacksListTimeRangeErrorComponentCode:
    if value in API_V1_APM_APMSTACKS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
