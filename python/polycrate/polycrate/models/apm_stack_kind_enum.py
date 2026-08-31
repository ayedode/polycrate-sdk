from typing import Literal

APMStackKindEnum = Literal["generic"]

APM_STACK_KIND_ENUM_VALUES: set[APMStackKindEnum] = {
    "generic",
}


def check_apm_stack_kind_enum(value: str) -> APMStackKindEnum:
    if value in APM_STACK_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APM_STACK_KIND_ENUM_VALUES!r}")
