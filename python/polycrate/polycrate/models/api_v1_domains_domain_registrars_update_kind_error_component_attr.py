from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_domain_registrars_update_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
