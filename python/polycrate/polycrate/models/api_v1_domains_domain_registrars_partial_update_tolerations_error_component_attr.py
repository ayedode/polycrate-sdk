from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_domain_registrars_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
