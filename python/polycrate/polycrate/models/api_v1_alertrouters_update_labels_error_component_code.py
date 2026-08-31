from typing import Literal

ApiV1AlertroutersUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ALERTROUTERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertroutersUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_alertrouters_update_labels_error_component_code(
    value: str,
) -> ApiV1AlertroutersUpdateLabelsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
