from typing import Literal

ApiV1PoliciesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_POLICIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PoliciesCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_policies_create_labels_error_component_code(value: str) -> ApiV1PoliciesCreateLabelsErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
