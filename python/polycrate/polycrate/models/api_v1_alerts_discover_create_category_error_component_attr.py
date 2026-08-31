from typing import Literal

ApiV1AlertsDiscoverCreateCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTS_DISCOVER_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateCategoryErrorComponentAttr
] = {
    "category",
}


def check_api_v1_alerts_discover_create_category_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateCategoryErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
