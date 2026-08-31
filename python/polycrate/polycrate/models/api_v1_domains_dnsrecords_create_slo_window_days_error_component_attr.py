from typing import Literal

ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_DOMAINS_DNSRECORDS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_domains_dnsrecords_create_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateSloWindowDaysErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
