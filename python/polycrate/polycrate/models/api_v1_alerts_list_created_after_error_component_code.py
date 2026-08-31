from typing import Literal

ApiV1AlertsListCreatedAfterErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_LIST_CREATED_AFTER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsListCreatedAfterErrorComponentCode] = {
    "invalid",
}


def check_api_v1_alerts_list_created_after_error_component_code(
    value: str,
) -> ApiV1AlertsListCreatedAfterErrorComponentCode:
    if value in API_V1_ALERTS_LIST_CREATED_AFTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_LIST_CREATED_AFTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
