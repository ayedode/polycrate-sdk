from typing import Literal

ApiV1AlertroutersCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ALERTROUTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_alertrouters_create_annotations_error_component_code(
    value: str,
) -> ApiV1AlertroutersCreateAnnotationsErrorComponentCode:
    if value in API_V1_ALERTROUTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
