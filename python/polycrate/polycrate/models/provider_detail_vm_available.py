from typing import Literal

ProviderDetailVmAvailable = Literal["", "no", "planned", "yes"]

PROVIDER_DETAIL_VM_AVAILABLE_VALUES: set[ProviderDetailVmAvailable] = {
    "",
    "no",
    "planned",
    "yes",
}


def check_provider_detail_vm_available(value: str) -> ProviderDetailVmAvailable:
    if value in PROVIDER_DETAIL_VM_AVAILABLE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_VM_AVAILABLE_VALUES!r}")
