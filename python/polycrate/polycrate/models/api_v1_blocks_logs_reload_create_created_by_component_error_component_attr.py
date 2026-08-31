from typing import Literal

ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_blocks_logs_reload_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
