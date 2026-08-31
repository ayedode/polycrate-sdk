from typing import Literal

ApiV1BlocksLogsReloadCreateActionsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateActionsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_logs_reload_create_actions_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateActionsErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_ACTIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
