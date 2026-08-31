from typing import Literal

ApiV1BlocksLogsReloadCreateTemplateErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateTemplateErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_logs_reload_create_template_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateTemplateErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
