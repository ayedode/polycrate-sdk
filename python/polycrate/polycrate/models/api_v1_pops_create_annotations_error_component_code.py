from typing import Literal

ApiV1PopsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_POPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsCreateAnnotationsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_pops_create_annotations_error_component_code(
    value: str,
) -> ApiV1PopsCreateAnnotationsErrorComponentCode:
    if value in API_V1_POPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
