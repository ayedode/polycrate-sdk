from typing import Literal

ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_logs_reload_create_is_behind_stable_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateIsBehindStableErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
