from typing import Literal

ApiV1WorkspacesPartialUpdatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_partial_update_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
