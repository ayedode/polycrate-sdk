from typing import Literal

ApiV1CvesArchiveCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_CVES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesArchiveCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_cves_archive_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
