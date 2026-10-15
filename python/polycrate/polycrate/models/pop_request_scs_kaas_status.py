from typing import Literal

PopRequestScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

POP_REQUEST_SCS_KAAS_STATUS_VALUES: set[PopRequestScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_pop_request_scs_kaas_status(value: str) -> PopRequestScsKaasStatus:
    if value in POP_REQUEST_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_SCS_KAAS_STATUS_VALUES!r}")
