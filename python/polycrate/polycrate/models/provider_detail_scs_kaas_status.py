from typing import Literal

ProviderDetailScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

PROVIDER_DETAIL_SCS_KAAS_STATUS_VALUES: set[ProviderDetailScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_provider_detail_scs_kaas_status(value: str) -> ProviderDetailScsKaasStatus:
    if value in PROVIDER_DETAIL_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_SCS_KAAS_STATUS_VALUES!r}")
