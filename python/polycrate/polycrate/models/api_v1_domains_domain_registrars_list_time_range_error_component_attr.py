from typing import Literal

ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_domains_domain_registrars_list_time_range_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListTimeRangeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
