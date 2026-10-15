from typing import Literal

PatchedProviderDetailRequestScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

PATCHED_PROVIDER_DETAIL_REQUEST_SCS_IAAS_STATUS_VALUES: set[PatchedProviderDetailRequestScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_patched_provider_detail_request_scs_iaas_status(value: str) -> PatchedProviderDetailRequestScsIaasStatus:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_SCS_IAAS_STATUS_VALUES!r}"
    )
