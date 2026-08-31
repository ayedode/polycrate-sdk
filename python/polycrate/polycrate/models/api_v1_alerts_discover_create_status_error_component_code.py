from typing import Literal

ApiV1AlertsDiscoverCreateStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTS_DISCOVER_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateStatusErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alerts_discover_create_status_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateStatusErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
