from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_domains_domain_registrars_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
