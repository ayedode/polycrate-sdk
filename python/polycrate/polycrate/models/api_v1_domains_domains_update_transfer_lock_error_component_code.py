from typing import Literal

ApiV1DomainsDomainsUpdateTransferLockErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsUpdateTransferLockErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_update_transfer_lock_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsUpdateTransferLockErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
