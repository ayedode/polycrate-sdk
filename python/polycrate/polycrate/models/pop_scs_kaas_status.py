from typing import Literal

PopScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

POP_SCS_KAAS_STATUS_VALUES: set[PopScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_pop_scs_kaas_status(value: str) -> PopScsKaasStatus:
    if value in POP_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_SCS_KAAS_STATUS_VALUES!r}")
