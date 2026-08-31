from typing import Literal

ApiV1AlertsUpdateCategoryErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTS_UPDATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateCategoryErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alerts_update_category_error_component_code(value: str) -> ApiV1AlertsUpdateCategoryErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
