from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_domains_domain_registrars_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
