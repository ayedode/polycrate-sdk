from typing import Literal

ApiV1BlocksLogsReloadCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_blocks_logs_reload_create_kind_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateKindErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
