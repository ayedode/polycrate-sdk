from typing import Literal

ApiV1DowntimesListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_DOWNTIMES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesListTimeRangeErrorComponentAttr] = {
    "time_range",
}


def check_api_v1_downtimes_list_time_range_error_component_attr(
    value: str,
) -> ApiV1DowntimesListTimeRangeErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
