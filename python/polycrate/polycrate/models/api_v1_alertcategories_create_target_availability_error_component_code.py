from typing import Literal

ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_ALERTCATEGORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_alertcategories_create_target_availability_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
