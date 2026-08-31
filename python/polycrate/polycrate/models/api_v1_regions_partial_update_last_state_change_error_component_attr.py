from typing import Literal

ApiV1RegionsPartialUpdateLastStateChangeErrorComponentAttr = Literal["last_state_change"]

API_V1_REGIONS_PARTIAL_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateLastStateChangeErrorComponentAttr
] = {
    "last_state_change",
}


def check_api_v1_regions_partial_update_last_state_change_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateLastStateChangeErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_LAST_STATE_CHANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
