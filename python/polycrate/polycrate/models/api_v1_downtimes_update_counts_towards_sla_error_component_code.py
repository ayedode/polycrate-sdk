from typing import Literal

ApiV1DowntimesUpdateCountsTowardsSlaErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_UPDATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesUpdateCountsTowardsSlaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_update_counts_towards_sla_error_component_code(
    value: str,
) -> ApiV1DowntimesUpdateCountsTowardsSlaErrorComponentCode:
    if value in API_V1_DOWNTIMES_UPDATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
