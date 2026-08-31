from typing import Literal

ApiV1RegionsUpdateLastStateChangeErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_REGIONS_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsUpdateLastStateChangeErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_regions_update_last_state_change_error_component_code(
    value: str,
) -> ApiV1RegionsUpdateLastStateChangeErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
