from typing import Literal

ApiV1DomainsDnsrecordsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_DOMAINS_DNSRECORDS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_domains_dnsrecords_list_time_range_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsListTimeRangeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
