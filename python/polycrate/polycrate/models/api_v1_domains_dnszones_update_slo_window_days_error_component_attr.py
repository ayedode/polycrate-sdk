from typing import Literal

ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_DOMAINS_DNSZONES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_domains_dnszones_update_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateSloWindowDaysErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
