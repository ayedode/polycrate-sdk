from typing import Literal

APMStackKind = Literal["generic"]

APM_STACK_KIND_VALUES: set[APMStackKind] = {
    "generic",
}


def check_apm_stack_kind(value: str) -> APMStackKind:
    if value in APM_STACK_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APM_STACK_KIND_VALUES!r}")
