from typing import Literal

ApiV1AlertsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_alerts_update_labels_error_component_code(value: str) -> ApiV1AlertsUpdateLabelsErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
