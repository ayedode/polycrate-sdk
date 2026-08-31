from typing import Literal

ApiV1AlertcategoryMappingsPartialUpdateMatchTypeErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_MATCH_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryMappingsPartialUpdateMatchTypeErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_alertcategory_mappings_partial_update_match_type_error_component_code(
    value: str,
) -> ApiV1AlertcategoryMappingsPartialUpdateMatchTypeErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_MATCH_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_MATCH_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
