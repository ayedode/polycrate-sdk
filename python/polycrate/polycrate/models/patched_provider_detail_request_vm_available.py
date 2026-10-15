from typing import Literal

PatchedProviderDetailRequestVmAvailable = Literal["", "no", "planned", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_VM_AVAILABLE_VALUES: set[PatchedProviderDetailRequestVmAvailable] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_patched_provider_detail_request_vm_available(value: str) -> PatchedProviderDetailRequestVmAvailable:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_VM_AVAILABLE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_VM_AVAILABLE_VALUES!r}"
    )
