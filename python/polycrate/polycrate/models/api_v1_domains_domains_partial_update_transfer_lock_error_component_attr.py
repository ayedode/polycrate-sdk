from typing import Literal

ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponentAttr = Literal["transfer_lock"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponentAttr
] = {
    "transfer_lock",
}


def check_api_v1_domains_domains_partial_update_transfer_lock_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateTransferLockErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
