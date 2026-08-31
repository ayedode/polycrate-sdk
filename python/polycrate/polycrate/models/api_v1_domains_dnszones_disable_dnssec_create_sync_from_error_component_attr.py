from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponentAttr = Literal["sync_from"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SYNC_FROM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponentAttr
] = {
    "sync_from",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_sync_from_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SYNC_FROM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SYNC_FROM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
