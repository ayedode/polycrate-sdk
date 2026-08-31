from typing import Literal

ApiV1WorkspacesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1WorkspacesUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_update_kind_error_component_code(value: str) -> ApiV1WorkspacesUpdateKindErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
