from typing import Literal

ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_domains_domains_archive_create_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
