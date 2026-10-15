from typing import Literal

PatchedPopRequestScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

PATCHED_POP_REQUEST_SCS_KAAS_STATUS_VALUES: set[PatchedPopRequestScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_patched_pop_request_scs_kaas_status(value: str) -> PatchedPopRequestScsKaasStatus:
    if value in PATCHED_POP_REQUEST_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_SCS_KAAS_STATUS_VALUES!r}")
