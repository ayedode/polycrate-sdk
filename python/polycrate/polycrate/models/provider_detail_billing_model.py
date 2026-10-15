from typing import Literal

ProviderDetailBillingModel = Literal["", "both", "monthly", "usage"]

PROVIDER_DETAIL_BILLING_MODEL_VALUES: set[ProviderDetailBillingModel] = {
    "",
    "both",
    "monthly",
    "usage",
}


def check_provider_detail_billing_model(value: str) -> ProviderDetailBillingModel:
    if value in PROVIDER_DETAIL_BILLING_MODEL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_BILLING_MODEL_VALUES!r}")
