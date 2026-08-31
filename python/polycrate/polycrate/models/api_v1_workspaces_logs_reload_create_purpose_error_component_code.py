from typing import Literal

ApiV1WorkspacesLogsReloadCreatePurposeErrorComponentCode = Literal["invalid_choice"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreatePurposeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_workspaces_logs_reload_create_purpose_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreatePurposeErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
