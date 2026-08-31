from typing import Literal

ApiV1LoadbalancersRegionsListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_LOADBALANCERS_REGIONS_LIST_TIME_RANGE_VALUES: set[ApiV1LoadbalancersRegionsListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_loadbalancers_regions_list_time_range(value: str) -> ApiV1LoadbalancersRegionsListTimeRange:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_TIME_RANGE_VALUES!r}"
    )
