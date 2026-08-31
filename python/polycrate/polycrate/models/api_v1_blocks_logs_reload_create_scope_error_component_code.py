from typing import Literal

ApiV1BlocksLogsReloadCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_blocks_logs_reload_create_scope_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateScopeErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
