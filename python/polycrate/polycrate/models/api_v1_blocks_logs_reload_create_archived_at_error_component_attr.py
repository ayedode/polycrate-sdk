from typing import Literal

ApiV1BlocksLogsReloadCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_blocks_logs_reload_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateArchivedAtErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
