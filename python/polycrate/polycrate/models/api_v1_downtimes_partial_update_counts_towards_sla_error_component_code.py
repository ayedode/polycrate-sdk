from typing import Literal

ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_partial_update_counts_towards_sla_error_component_code(
    value: str,
) -> ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponentCode:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
