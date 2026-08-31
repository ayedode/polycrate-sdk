from typing import Literal

ApiV1AlertsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ALERTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_alerts_update_kind_error_component_code(value: str) -> ApiV1AlertsUpdateKindErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
