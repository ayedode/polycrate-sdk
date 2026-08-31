from typing import Literal

ApiV1PoliciesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_POLICIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_policies_create_annotations_error_component_code(
    value: str,
) -> ApiV1PoliciesCreateAnnotationsErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
