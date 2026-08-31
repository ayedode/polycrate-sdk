from typing import Literal

ApiV1SecretmanagerManagersListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_SECRETMANAGER_MANAGERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_secretmanager_managers_list_time_range_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersListTimeRangeErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
