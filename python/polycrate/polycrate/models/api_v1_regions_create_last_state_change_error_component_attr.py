from typing import Literal

ApiV1RegionsCreateLastStateChangeErrorComponentAttr = Literal["last_state_change"]

API_V1_REGIONS_CREATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsCreateLastStateChangeErrorComponentAttr
] = {
    "last_state_change",
}


def check_api_v1_regions_create_last_state_change_error_component_attr(
    value: str,
) -> ApiV1RegionsCreateLastStateChangeErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
