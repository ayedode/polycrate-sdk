from typing import Literal

ApiV1AlertsCreateCategoryErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTS_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsCreateCategoryErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alerts_create_category_error_component_code(value: str) -> ApiV1AlertsCreateCategoryErrorComponentCode:
    if value in API_V1_ALERTS_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_CATEGORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
