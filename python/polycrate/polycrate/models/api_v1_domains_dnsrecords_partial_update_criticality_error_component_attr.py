from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_dnsrecords_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
