from typing import Literal

ApiV1AlertsPartialUpdateStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_ALERTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateStatusErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_alerts_partial_update_status_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateStatusErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
