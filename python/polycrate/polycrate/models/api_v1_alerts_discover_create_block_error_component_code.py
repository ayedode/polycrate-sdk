from typing import Literal

ApiV1AlertsDiscoverCreateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsDiscoverCreateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_discover_create_block_error_component_code(
    value: str,
) -> ApiV1AlertsDiscoverCreateBlockErrorComponentCode:
    if value in API_V1_ALERTS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
