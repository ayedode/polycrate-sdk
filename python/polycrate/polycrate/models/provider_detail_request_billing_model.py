from typing import Literal

ProviderDetailRequestBillingModel = Literal["", "both", "monthly", "usage"]

PROVIDER_DETAIL_REQUEST_BILLING_MODEL_VALUES: set[ProviderDetailRequestBillingModel] = {
    "",
    "both",
    "monthly",
    "usage",
}


def check_provider_detail_request_billing_model(value: str) -> ProviderDetailRequestBillingModel:
    if value in PROVIDER_DETAIL_REQUEST_BILLING_MODEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_BILLING_MODEL_VALUES!r}")
