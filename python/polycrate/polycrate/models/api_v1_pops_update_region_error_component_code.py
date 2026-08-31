from typing import Literal

ApiV1PopsUpdateRegionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POPS_UPDATE_REGION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsUpdateRegionErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pops_update_region_error_component_code(value: str) -> ApiV1PopsUpdateRegionErrorComponentCode:
    if value in API_V1_POPS_UPDATE_REGION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_REGION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
