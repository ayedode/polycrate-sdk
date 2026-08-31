from typing import Literal

ApiV1ConditionsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CONDITIONS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ConditionsCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_conditions_create_labels_error_component_code(
    value: str,
) -> ApiV1ConditionsCreateLabelsErrorComponentCode:
    if value in API_V1_CONDITIONS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
