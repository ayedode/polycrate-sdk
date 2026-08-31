from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_ds_delegation_synced_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
