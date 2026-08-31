from typing import Literal

ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_endpoints_archive_create_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateSloWindowDaysErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
