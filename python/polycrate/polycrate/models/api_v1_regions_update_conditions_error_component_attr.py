from typing import Literal

ApiV1RegionsUpdateConditionsErrorComponentAttr = Literal["conditions"]

API_V1_REGIONS_UPDATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsUpdateConditionsErrorComponentAttr] = {
    "conditions",
}


def check_api_v1_regions_update_conditions_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdateConditionsErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
