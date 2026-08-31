from typing import Literal

ApiV1RegionsCreateConditionsErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsCreateConditionsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_regions_create_conditions_error_component_code(
    value: str,
) -> ApiV1RegionsCreateConditionsErrorComponentCode:
    if value in API_V1_REGIONS_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
