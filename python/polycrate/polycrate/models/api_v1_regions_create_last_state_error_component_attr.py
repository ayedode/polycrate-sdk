from typing import Literal

ApiV1RegionsCreateLastStateErrorComponentAttr = Literal["last_state"]

API_V1_REGIONS_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsCreateLastStateErrorComponentAttr] = {
    "last_state",
}


def check_api_v1_regions_create_last_state_error_component_attr(
    value: str,
) -> ApiV1RegionsCreateLastStateErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
