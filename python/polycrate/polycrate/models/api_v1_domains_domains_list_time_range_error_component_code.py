from typing import Literal

ApiV1DomainsDomainsListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_DOMAINS_DOMAINS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_domains_domains_list_time_range_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsListTimeRangeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
