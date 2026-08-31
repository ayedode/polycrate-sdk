from typing import Literal

ApiV1AlertsListCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTS_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsListCategoryErrorComponentAttr] = {
    "category",
}


def check_api_v1_alerts_list_category_error_component_attr(value: str) -> ApiV1AlertsListCategoryErrorComponentAttr:
    if value in API_V1_ALERTS_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
