from typing import Literal

ApiV1ApmApmstacksListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_APM_APMSTACKS_LIST_TIME_RANGE_VALUES: set[ApiV1ApmApmstacksListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_apm_apmstacks_list_time_range(value: str) -> ApiV1ApmApmstacksListTimeRange:
    if value in API_V1_APM_APMSTACKS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_TIME_RANGE_VALUES!r}")
