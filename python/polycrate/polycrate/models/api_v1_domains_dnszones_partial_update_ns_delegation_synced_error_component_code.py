from typing import Literal

ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_NS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_partial_update_ns_delegation_synced_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateNsDelegationSyncedErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_NS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_NS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
