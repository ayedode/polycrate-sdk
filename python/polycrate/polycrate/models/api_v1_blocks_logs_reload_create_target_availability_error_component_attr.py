from typing import Literal

ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_blocks_logs_reload_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
