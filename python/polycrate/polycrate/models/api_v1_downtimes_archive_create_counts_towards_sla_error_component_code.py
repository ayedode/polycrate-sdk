from typing import Literal

ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponentCode = Literal["invalid", "null"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_downtimes_archive_create_counts_towards_sla_error_component_code(
    value: str,
) -> ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponentCode:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
