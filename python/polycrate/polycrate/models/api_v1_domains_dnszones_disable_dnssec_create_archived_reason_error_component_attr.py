from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
