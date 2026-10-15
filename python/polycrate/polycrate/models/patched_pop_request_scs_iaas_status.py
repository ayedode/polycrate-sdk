from typing import Literal

PatchedPopRequestScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

PATCHED_POP_REQUEST_SCS_IAAS_STATUS_VALUES: set[PatchedPopRequestScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_patched_pop_request_scs_iaas_status(value: str) -> PatchedPopRequestScsIaasStatus:
    if value in PATCHED_POP_REQUEST_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_SCS_IAAS_STATUS_VALUES!r}")
