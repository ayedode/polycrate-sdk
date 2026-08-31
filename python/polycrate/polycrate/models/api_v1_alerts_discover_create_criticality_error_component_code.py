from typing import Literal

ApiV1AlertsDiscoverCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alerts_discover_create_criticality_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateCriticalityErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
