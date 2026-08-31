from typing import Literal

ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponentAttr = Literal["dnssec_ds_records"]

API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_DS_RECORDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponentAttr
] = {
    "dnssec_ds_records",
}


def check_api_v1_domains_dnszones_update_dnssec_ds_records_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateDnssecDsRecordsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_DS_RECORDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_DS_RECORDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
