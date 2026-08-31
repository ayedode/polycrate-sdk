from typing import Literal

ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponentAttr = Literal["category_id"]

API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponentAttr
] = {
    "category_id",
}


def check_api_v1_alertcategory_mappings_update_category_id_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsUpdateCategoryIdErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_UPDATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
