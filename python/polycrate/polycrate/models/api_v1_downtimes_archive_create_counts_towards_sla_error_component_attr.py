from typing import Literal

ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponentAttr = Literal["counts_towards_sla"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponentAttr
] = {
    "counts_towards_sla",
}


def check_api_v1_downtimes_archive_create_counts_towards_sla_error_component_attr(
    value: str,
) -> ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponentAttr:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_COUNTS_TOWARDS_SLA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
