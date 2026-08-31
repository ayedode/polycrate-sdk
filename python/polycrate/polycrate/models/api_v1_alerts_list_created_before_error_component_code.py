from typing import Literal

ApiV1AlertsListCreatedBeforeErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_LIST_CREATED_BEFORE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsListCreatedBeforeErrorComponentCode] = {
    "invalid",
}


def check_api_v1_alerts_list_created_before_error_component_code(
    value: str,
) -> ApiV1AlertsListCreatedBeforeErrorComponentCode:
    if value in API_V1_ALERTS_LIST_CREATED_BEFORE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_CREATED_BEFORE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
