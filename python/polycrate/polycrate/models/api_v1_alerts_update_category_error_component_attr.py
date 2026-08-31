from typing import Literal

ApiV1AlertsUpdateCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTS_UPDATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateCategoryErrorComponentAttr] = {
    "category",
}


def check_api_v1_alerts_update_category_error_component_attr(value: str) -> ApiV1AlertsUpdateCategoryErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
