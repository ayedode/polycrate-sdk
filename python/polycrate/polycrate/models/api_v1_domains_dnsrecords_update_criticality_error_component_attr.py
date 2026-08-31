from typing import Literal

ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DNSRECORDS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_dnsrecords_update_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
