from typing import Literal

ApiV1AlertsListCategoryErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_ALERTS_LIST_CATEGORY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsListCategoryErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_alerts_list_category_error_component_code(value: str) -> ApiV1AlertsListCategoryErrorComponentCode:
    if value in API_V1_ALERTS_LIST_CATEGORY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_CATEGORY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
