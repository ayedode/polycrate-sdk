from typing import Literal

ApiV1DowntimesPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_downtimes_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1DowntimesPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
