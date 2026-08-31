from typing import Literal

ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_DOMAINS_DNSRECORDS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_domains_dnsrecords_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
