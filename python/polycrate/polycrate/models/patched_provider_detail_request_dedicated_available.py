from typing import Literal

PatchedProviderDetailRequestDedicatedAvailable = Literal["", "no", "planned", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_DEDICATED_AVAILABLE_VALUES: set[PatchedProviderDetailRequestDedicatedAvailable] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_patched_provider_detail_request_dedicated_available(
    value: str,
) -> PatchedProviderDetailRequestDedicatedAvailable:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_DEDICATED_AVAILABLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_DEDICATED_AVAILABLE_VALUES!r}"
    )
