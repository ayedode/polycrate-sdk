from typing import Literal

ApiV1AlertsCreateCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTS_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateCategoryErrorComponentAttr] = {
    "category",
}


def check_api_v1_alerts_create_category_error_component_attr(value: str) -> ApiV1AlertsCreateCategoryErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
