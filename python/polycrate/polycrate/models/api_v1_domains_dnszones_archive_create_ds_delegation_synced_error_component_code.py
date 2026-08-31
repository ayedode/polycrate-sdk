from typing import Literal

ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_archive_create_ds_delegation_synced_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
