from typing import Literal

ProviderDetailRequestBlockStorageStatus = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_BLOCK_STORAGE_STATUS_VALUES: set[ProviderDetailRequestBlockStorageStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_block_storage_status(value: str) -> ProviderDetailRequestBlockStorageStatus:
    if value in PROVIDER_DETAIL_REQUEST_BLOCK_STORAGE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_BLOCK_STORAGE_STATUS_VALUES!r}"
    )
