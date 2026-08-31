from typing import Literal

ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_archive_create_transfer_lock_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
