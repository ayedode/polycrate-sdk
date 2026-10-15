from typing import Literal

PatchedProviderDetailRequestScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

PATCHED_PROVIDER_DETAIL_REQUEST_SCS_KAAS_STATUS_VALUES: set[PatchedProviderDetailRequestScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_patched_provider_detail_request_scs_kaas_status(value: str) -> PatchedProviderDetailRequestScsKaasStatus:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_SCS_KAAS_STATUS_VALUES!r}"
    )
