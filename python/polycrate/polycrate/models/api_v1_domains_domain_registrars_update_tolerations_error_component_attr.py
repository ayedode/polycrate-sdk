from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_domain_registrars_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
