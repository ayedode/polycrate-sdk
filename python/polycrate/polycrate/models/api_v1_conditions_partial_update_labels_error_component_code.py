from typing import Literal

ApiV1ConditionsPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CONDITIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_conditions_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1ConditionsPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
