from typing import Literal

ApiV1AlertsPartialUpdateCategoryErrorComponentAttr = Literal["category"]

API_V1_ALERTS_PARTIAL_UPDATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateCategoryErrorComponentAttr
] = {
    "category",
}


def check_api_v1_alerts_partial_update_category_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateCategoryErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_CATEGORY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
