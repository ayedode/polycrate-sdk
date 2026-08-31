from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponentAttr = Literal["dnssec_ds_records"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_DS_RECORDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponentAttr
] = {
    "dnssec_ds_records",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_dnssec_ds_records_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_DS_RECORDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_DS_RECORDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
