from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponentAttr = Literal["ote"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_OTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponentAttr
] = {
    "ote",
}


def check_api_v1_domains_domain_registrars_partial_update_ote_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateOteErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_OTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_OTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
