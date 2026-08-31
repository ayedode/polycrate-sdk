from typing import Literal

ApiV1AlertcategoryMappingsListCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTCATEGORY_MAPPINGS_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryMappingsListCategoryErrorComponentAttr
] = {
    "category",
}


def check_api_v1_alertcategory_mappings_list_category_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryMappingsListCategoryErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_MAPPINGS_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_MAPPINGS_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
