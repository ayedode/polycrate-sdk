from typing import Literal

ApiV1AlertsDiscoverCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alerts_discover_create_tolerations_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateTolerationsErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
