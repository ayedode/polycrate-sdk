from typing import Literal

ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponentAttr = Literal["sort_order"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponentAttr
] = {
    "sort_order",
}


def check_api_v1_alertcategories_partial_update_sort_order_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateSortOrderErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
