from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_domains_domain_registrars_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
