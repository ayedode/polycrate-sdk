from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_domains_domain_registrars_partial_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
