from typing import Literal

ApiV1BlocksLogsReloadCreateFullSpecErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateFullSpecErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_logs_reload_create_full_spec_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateFullSpecErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_FULL_SPEC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
