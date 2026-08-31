from typing import Literal

ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_partial_update_transfer_lock_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
