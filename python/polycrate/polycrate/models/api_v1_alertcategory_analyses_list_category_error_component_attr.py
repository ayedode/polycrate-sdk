from typing import Literal

ApiV1AlertcategoryAnalysesListCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTCATEGORY_ANALYSES_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoryAnalysesListCategoryErrorComponentAttr
] = {
    "category",
}


def check_api_v1_alertcategory_analyses_list_category_error_component_attr(
    value: str,
) -> ApiV1AlertcategoryAnalysesListCategoryErrorComponentAttr:
    if value in API_V1_ALERTCATEGORY_ANALYSES_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORY_ANALYSES_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
