from typing import Literal

ApiV1AlertsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ALERTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alerts_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
