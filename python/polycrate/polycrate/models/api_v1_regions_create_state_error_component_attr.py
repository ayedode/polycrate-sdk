from typing import Literal

ApiV1RegionsCreateStateErrorComponentAttr = Literal["state"]

API_V1_REGIONS_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsCreateStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_regions_create_state_error_component_attr(value: str) -> ApiV1RegionsCreateStateErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
