from typing import Literal

ApiV1ConditionsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CONDITIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_conditions_update_annotations_error_component_code(
    value: str,
) -> ApiV1ConditionsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_CONDITIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
