from typing import Literal

ApiV1AlertcategoryMappingsPartialUpdateCategoryIdErrorComponentAttr = Literal["category_id"]

API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsPartialUpdateCategoryIdErrorComponentAttr
] = {
    "category_id",
}


def check_api_v1_alertcategory_mappings_partial_update_category_id_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsPartialUpdateCategoryIdErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_PARTIAL_UPDATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
