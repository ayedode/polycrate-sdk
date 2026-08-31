from typing import Literal

ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_domains_domain_registrars_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListUpdatedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
