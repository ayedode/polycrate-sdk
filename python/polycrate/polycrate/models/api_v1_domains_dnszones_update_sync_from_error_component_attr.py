from typing import Literal

ApiV1DomainsDnszonesUpdateSyncFromErrorComponentAttr = Literal["sync_from"]

API_V1_DOMAINS_DNSZONES_UPDATE_SYNC_FROM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateSyncFromErrorComponentAttr
] = {
    "sync_from",
}


def check_api_v1_domains_dnszones_update_sync_from_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateSyncFromErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_SYNC_FROM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_SYNC_FROM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
