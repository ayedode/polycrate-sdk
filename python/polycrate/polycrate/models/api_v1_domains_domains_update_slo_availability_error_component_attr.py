from typing import Literal

ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_DOMAINS_DOMAINS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_domains_domains_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
