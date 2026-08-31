from typing import Literal

ApiV1AlertcategoryMappingsPartialUpdatePriorityErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryMappingsPartialUpdatePriorityErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_alertcategory_mappings_partial_update_priority_error_component_code(
    value: str,
) -> ApiV1AlertcategoryMappingsPartialUpdatePriorityErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_PRIORITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
