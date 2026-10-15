from typing import Literal

PatchedProviderDetailRequestBillingModel = Literal["", "both", "monthly", "usage"]

PATCHED_PROVIDER_DETAIL_REQUEST_BILLING_MODEL_VALUES: set[PatchedProviderDetailRequestBillingModel] = {
    "",
    "both",
    "monthly",
    "usage",
}


def check_patched_provider_detail_request_billing_model(value: str) -> PatchedProviderDetailRequestBillingModel:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_BILLING_MODEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_BILLING_MODEL_VALUES!r}"
    )
