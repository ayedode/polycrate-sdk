from typing import Literal

ApiV1AlertcategoriesCreateSortOrderErrorComponentAttr = Literal["sort_order"]

API_V1_ALERTCATEGORIES_CREATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateSortOrderErrorComponentAttr
] = {
    "sort_order",
}


def check_api_v1_alertcategories_create_sort_order_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateSortOrderErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
