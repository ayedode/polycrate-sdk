from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_domain_registrars_update_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
