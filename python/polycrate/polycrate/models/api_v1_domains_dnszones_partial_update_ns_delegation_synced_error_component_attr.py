from typing import Literal

ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponentAttr = Literal["ns_delegation_synced"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_NS_DELEGATION_SYNCED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponentAttr
] = {
    "ns_delegation_synced",
}


def check_api_v1_domains_dnszones_partial_update_ns_delegation_synced_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_NS_DELEGATION_SYNCED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_NS_DELEGATION_SYNCED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
