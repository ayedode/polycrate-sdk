from typing import Literal

ApiV1AlertcategoryMappingsCreateCategoryIdErrorComponentAttr = Literal["category_id"]

API_V1_ALERTCATEGORY_MAPPINGS_CREATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsCreateCategoryIdErrorComponentAttr
] = {
    "category_id",
}


def check_api_v1_alertcategory_mappings_create_category_id_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsCreateCategoryIdErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_CREATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_CREATE_CATEGORY_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
