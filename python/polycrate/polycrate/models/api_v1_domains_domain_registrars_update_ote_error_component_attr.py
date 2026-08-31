from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateOteErrorComponentAttr = Literal["ote"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_OTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateOteErrorComponentAttr
] = {
    "ote",
}


def check_api_v1_domains_domain_registrars_update_ote_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateOteErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_OTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_OTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
