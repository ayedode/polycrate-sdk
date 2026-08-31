from typing import Literal

ApiV1BlocksLogsReloadCreateTypeErrorComponentAttr = Literal["type"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateTypeErrorComponentAttr
] = {
    "type",
}


def check_api_v1_blocks_logs_reload_create_type_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateTypeErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
