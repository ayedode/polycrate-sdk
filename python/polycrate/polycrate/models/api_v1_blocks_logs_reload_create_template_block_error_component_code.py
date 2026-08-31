from typing import Literal

ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_blocks_logs_reload_create_template_block_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateTemplateBlockErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
