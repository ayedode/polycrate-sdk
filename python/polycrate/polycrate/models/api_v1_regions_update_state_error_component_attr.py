from typing import Literal

ApiV1RegionsUpdateStateErrorComponentAttr = Literal["state"]

API_V1_REGIONS_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsUpdateStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_regions_update_state_error_component_attr(value: str) -> ApiV1RegionsUpdateStateErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
