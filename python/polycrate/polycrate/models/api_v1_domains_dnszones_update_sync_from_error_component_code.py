from typing import Literal

ApiV1DomainsDnszonesUpdateSyncFromErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DNSZONES_UPDATE_SYNC_FROM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesUpdateSyncFromErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_dnszones_update_sync_from_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesUpdateSyncFromErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_SYNC_FROM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_SYNC_FROM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
