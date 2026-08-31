from typing import Literal

ApiV1BlocksLogsReloadCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_blocks_logs_reload_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateSloTargetErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
