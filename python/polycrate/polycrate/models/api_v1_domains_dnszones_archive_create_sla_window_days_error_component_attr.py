from typing import Literal

ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_domains_dnszones_archive_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
