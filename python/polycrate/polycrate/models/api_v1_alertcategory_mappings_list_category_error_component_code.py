from typing import Literal

ApiV1AlertcategoryMappingsListCategoryErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTCATEGORY_MAPPINGS_LIST_CATEGORY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryMappingsListCategoryErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alertcategory_mappings_list_category_error_component_code(
    value: str,
) -> ApiV1AlertcategoryMappingsListCategoryErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_LIST_CATEGORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_LIST_CATEGORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
