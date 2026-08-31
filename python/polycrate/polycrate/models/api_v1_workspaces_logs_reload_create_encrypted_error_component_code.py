from typing import Literal

ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_logs_reload_create_encrypted_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateEncryptedErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ENCRYPTED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
