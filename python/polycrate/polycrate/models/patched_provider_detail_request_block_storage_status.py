from typing import Literal

PatchedProviderDetailRequestBlockStorageStatus = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_BLOCK_STORAGE_STATUS_VALUES: set[PatchedProviderDetailRequestBlockStorageStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_block_storage_status(
    value: str,
) -> PatchedProviderDetailRequestBlockStorageStatus:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_BLOCK_STORAGE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_BLOCK_STORAGE_STATUS_VALUES!r}"
    )
