from typing import Literal

ApiV1DomainsDomainsUpdateTransferLockErrorComponentAttr = Literal["transfer_lock"]

API_V1_DOMAINS_DOMAINS_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateTransferLockErrorComponentAttr
] = {
    "transfer_lock",
}


def check_api_v1_domains_domains_update_transfer_lock_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateTransferLockErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
