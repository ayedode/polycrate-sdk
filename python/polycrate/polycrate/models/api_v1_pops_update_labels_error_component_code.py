from typing import Literal

ApiV1PopsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_POPS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_pops_update_labels_error_component_code(value: str) -> ApiV1PopsUpdateLabelsErrorComponentCode:
    if value in API_V1_POPS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
