from typing import Literal

ApiV1RegionsCreateLastStateChangeErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_REGIONS_CREATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsCreateLastStateChangeErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_regions_create_last_state_change_error_component_code(
    value: str,
) -> ApiV1RegionsCreateLastStateChangeErrorComponentCode:
    if value in API_V1_REGIONS_CREATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
