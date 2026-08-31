from typing import Literal

ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_blocks_logs_reload_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
