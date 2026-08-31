from typing import Literal

ApiV1WorkspacesCheckCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_check_create_criticality_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateCriticalityErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
