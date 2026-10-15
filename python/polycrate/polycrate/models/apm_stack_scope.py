from typing import Literal

APMStackScope = Literal["system", "user"]

APM_STACK_SCOPE_VALUES: set[APMStackScope] = {
    "system",
    "user",
}


def check_apm_stack_scope(value: str) -> APMStackScope:
    if value in APM_STACK_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APM_STACK_SCOPE_VALUES!r}")
