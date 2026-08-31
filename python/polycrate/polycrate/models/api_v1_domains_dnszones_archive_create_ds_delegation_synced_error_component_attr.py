from typing import Literal

ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponentAttr = Literal["ds_delegation_synced"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponentAttr
] = {
    "ds_delegation_synced",
}


def check_api_v1_domains_dnszones_archive_create_ds_delegation_synced_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateDsDelegationSyncedErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DS_DELEGATION_SYNCED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
