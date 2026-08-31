from typing import Literal

ApiV1ConditionsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CONDITIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_conditions_create_annotations_error_component_code(
    value: str,
) -> ApiV1ConditionsCreateAnnotationsErrorComponentCode:
    if value in API_V1_CONDITIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
