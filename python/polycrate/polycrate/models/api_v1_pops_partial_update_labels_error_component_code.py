from typing import Literal

ApiV1PopsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_POPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsPartialUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_pops_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1PopsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_POPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
