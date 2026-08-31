from typing import Literal

ApiV1AlertcategoryMappingsListMatchTypeErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTCATEGORY_MAPPINGS_LIST_MATCH_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryMappingsListMatchTypeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alertcategory_mappings_list_match_type_error_component_code(
    value: str,
) -> ApiV1AlertcategoryMappingsListMatchTypeErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_LIST_MATCH_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_LIST_MATCH_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
