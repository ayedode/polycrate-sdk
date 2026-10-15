from typing import Literal

PopRequestScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

POP_REQUEST_SCS_IAAS_STATUS_VALUES: set[PopRequestScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_pop_request_scs_iaas_status(value: str) -> PopRequestScsIaasStatus:
    if value in POP_REQUEST_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_SCS_IAAS_STATUS_VALUES!r}")
