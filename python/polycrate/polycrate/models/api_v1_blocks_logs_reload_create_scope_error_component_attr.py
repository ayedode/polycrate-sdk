from typing import Literal

ApiV1BlocksLogsReloadCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_blocks_logs_reload_create_scope_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateScopeErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
