from typing import Literal

ApiV1PopsPartialUpdateLatitudeErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_POPS_PARTIAL_UPDATE_LATITUDE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsPartialUpdateLatitudeErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pops_partial_update_latitude_error_component_code(
    value: str,
) -> ApiV1PopsPartialUpdateLatitudeErrorComponentCode:
    if value in API_V1_POPS_PARTIAL_UPDATE_LATITUDE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_LATITUDE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
