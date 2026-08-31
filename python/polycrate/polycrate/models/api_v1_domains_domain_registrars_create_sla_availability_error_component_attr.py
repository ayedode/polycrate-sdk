from typing import Literal

ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_domains_domain_registrars_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
