from typing import Literal

ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_domains_dnsrecords_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDnsrecordsPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
