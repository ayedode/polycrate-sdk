from typing import Literal

PatchedProviderDetailRequestCloudInit = Literal["", "no", "planned", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_CLOUD_INIT_VALUES: set[PatchedProviderDetailRequestCloudInit] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_patched_provider_detail_request_cloud_init(value: str) -> PatchedProviderDetailRequestCloudInit:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_CLOUD_INIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_CLOUD_INIT_VALUES!r}"
    )
