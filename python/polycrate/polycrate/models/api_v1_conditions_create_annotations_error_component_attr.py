from typing import Literal

ApiV1ConditionsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CONDITIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_conditions_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ConditionsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CONDITIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
