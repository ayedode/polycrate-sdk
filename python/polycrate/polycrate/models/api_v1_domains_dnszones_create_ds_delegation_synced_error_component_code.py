from typing import Literal

ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_create_ds_delegation_synced_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
