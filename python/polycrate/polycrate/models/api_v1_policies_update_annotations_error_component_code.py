from typing import Literal

ApiV1PoliciesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_POLICIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_policies_update_annotations_error_component_code(
    value: str,
) -> ApiV1PoliciesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_POLICIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
