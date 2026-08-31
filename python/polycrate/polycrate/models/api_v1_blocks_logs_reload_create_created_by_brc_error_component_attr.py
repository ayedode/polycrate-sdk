from typing import Literal

ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponentAttr = Literal["created_by_brc"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponentAttr
] = {
    "created_by_brc",
}


def check_api_v1_blocks_logs_reload_create_created_by_brc_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateCreatedByBrcErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
