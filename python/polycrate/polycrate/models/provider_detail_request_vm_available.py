from typing import Literal

ProviderDetailRequestVmAvailable = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_REQUEST_VM_AVAILABLE_VALUES: set[ProviderDetailRequestVmAvailable] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_request_vm_available(value: str) -> ProviderDetailRequestVmAvailable:
    if value in PROVIDER_DETAIL_REQUEST_VM_AVAILABLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_VM_AVAILABLE_VALUES!r}")
