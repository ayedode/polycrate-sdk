from typing import Literal

ProviderDetailBlockStorageStatus = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_BLOCK_STORAGE_STATUS_VALUES: set[ProviderDetailBlockStorageStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_block_storage_status(value: str) -> ProviderDetailBlockStorageStatus:
    if value in PROVIDER_DETAIL_BLOCK_STORAGE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_BLOCK_STORAGE_STATUS_VALUES!r}")
