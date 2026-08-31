from typing import Literal

ApiV1DomainsDomainsCreateTransferLockErrorComponentAttr = Literal["transfer_lock"]

API_V1_DOMAINS_DOMAINS_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateTransferLockErrorComponentAttr
] = {
    "transfer_lock",
}


def check_api_v1_domains_domains_create_transfer_lock_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateTransferLockErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_TRANSFER_LOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
