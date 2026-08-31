from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_domain_registrars_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
