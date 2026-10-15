from typing import Literal

PopScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

POP_SCS_IAAS_STATUS_VALUES: set[PopScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_pop_scs_iaas_status(value: str) -> PopScsIaasStatus:
    if value in POP_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_SCS_IAAS_STATUS_VALUES!r}")
