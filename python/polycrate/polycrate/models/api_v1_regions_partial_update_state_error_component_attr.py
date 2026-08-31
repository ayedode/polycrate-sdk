from typing import Literal

ApiV1RegionsPartialUpdateStateErrorComponentAttr = Literal["state"]

API_V1_REGIONS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_regions_partial_update_state_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateStateErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
