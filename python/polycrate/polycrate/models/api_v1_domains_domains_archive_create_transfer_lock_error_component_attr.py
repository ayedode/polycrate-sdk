from typing import Literal

ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponentAttr = Literal["transfer_lock"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponentAttr
] = {
    "transfer_lock",
}


def check_api_v1_domains_domains_archive_create_transfer_lock_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
