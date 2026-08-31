from typing import Literal

ApiV1AlertcategoryMappingsUpdatePatternErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_PATTERN_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryMappingsUpdatePatternErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_alertcategory_mappings_update_pattern_error_component_code(
    value: str,
) -> ApiV1AlertcategoryMappingsUpdatePatternErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_PATTERN_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_PATTERN_ERROR_COMPONENT_CODE_VALUES!r}"
    )
