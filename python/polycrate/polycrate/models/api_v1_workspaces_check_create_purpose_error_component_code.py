from typing import Literal

ApiV1WorkspacesCheckCreatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_CHECK_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_check_create_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
