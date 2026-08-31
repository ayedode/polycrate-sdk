from typing import Literal

ApiV1DowntimesArchiveCreateExcludedReasonErrorComponentAttr = Literal["excluded_reason"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesArchiveCreateExcludedReasonErrorComponentAttr
] = {
    "excluded_reason",
}


def check_api_v1_downtimes_archive_create_excluded_reason_error_component_attr(
    value: str,
) -> ApiV1DowntimesArchiveCreateExcludedReasonErrorComponentAttr:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_EXCLUDED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
