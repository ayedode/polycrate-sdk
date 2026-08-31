from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
