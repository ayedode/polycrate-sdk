from typing import Literal

ApiV1PopsDiscoverCreateLongitudeErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_POPS_DISCOVER_CREATE_LONGITUDE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsDiscoverCreateLongitudeErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pops_discover_create_longitude_error_component_code(
    value: str,
) -> ApiV1PopsDiscoverCreateLongitudeErrorComponentCode:
    if value in API_V1_POPS_DISCOVER_CREATE_LONGITUDE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_LONGITUDE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
