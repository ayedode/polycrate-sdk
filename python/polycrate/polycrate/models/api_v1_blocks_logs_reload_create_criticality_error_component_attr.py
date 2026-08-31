from typing import Literal

ApiV1BlocksLogsReloadCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_blocks_logs_reload_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
