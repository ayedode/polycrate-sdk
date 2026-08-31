from typing import Literal

ApiV1BlocksLogsReloadCreateLatestStableErrorComponentAttr = Literal["latest_stable"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateLatestStableErrorComponentAttr
] = {
    "latest_stable",
}


def check_api_v1_blocks_logs_reload_create_latest_stable_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateLatestStableErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
