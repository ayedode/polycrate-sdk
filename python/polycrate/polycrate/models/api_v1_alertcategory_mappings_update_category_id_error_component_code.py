from typing import Literal

ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_CATEGORY_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_alertcategory_mappings_update_category_id_error_component_code(
    value: str,
) -> ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponentCode:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_CATEGORY_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_CATEGORY_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
