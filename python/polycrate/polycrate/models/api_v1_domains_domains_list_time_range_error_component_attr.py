from typing import Literal

ApiV1DomainsDomainsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_DOMAINS_DOMAINS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_domains_domains_list_time_range_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListTimeRangeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
