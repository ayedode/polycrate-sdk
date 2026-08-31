from typing import Literal

ApiV1BlocksLogsReloadCreateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_blocks_logs_reload_create_name_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateNameErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
