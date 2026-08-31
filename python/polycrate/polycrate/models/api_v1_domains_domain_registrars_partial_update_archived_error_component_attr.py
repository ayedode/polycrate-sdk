from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_domains_domain_registrars_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
