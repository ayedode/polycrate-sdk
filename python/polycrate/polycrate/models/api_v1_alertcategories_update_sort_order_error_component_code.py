from typing import Literal

ApiV1AlertcategoriesUpdateSortOrderErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_ALERTCATEGORIES_UPDATE_SORT_ORDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertcategoriesUpdateSortOrderErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_alertcategories_update_sort_order_error_component_code(
    value: str,
) -> ApiV1AlertcategoriesUpdateSortOrderErrorComponentCode:
    if value in API_V1_ALERTCATEGORIES_UPDATE_SORT_ORDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_UPDATE_SORT_ORDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
