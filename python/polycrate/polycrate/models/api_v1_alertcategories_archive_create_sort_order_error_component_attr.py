from typing import Literal

ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponentAttr = Literal["sort_order"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponentAttr
] = {
    "sort_order",
}


def check_api_v1_alertcategories_archive_create_sort_order_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_SORT_ORDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
