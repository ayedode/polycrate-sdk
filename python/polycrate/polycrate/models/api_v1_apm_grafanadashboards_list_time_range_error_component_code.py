from typing import Literal

ApiV1ApmGrafanadashboardsListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_APM_GRAFANADASHBOARDS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ApmGrafanadashboardsListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_apm_grafanadashboards_list_time_range_error_component_code(
    value: str,
) -> ApiV1ApmGrafanadashboardsListTimeRangeErrorComponentCode:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
