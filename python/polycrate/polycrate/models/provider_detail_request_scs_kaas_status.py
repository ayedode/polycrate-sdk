from typing import Literal

ProviderDetailRequestScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

PROVIDER_DETAIL_REQUEST_SCS_KAAS_STATUS_VALUES: set[ProviderDetailRequestScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_provider_detail_request_scs_kaas_status(value: str) -> ProviderDetailRequestScsKaasStatus:
    if value in PROVIDER_DETAIL_REQUEST_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_SCS_KAAS_STATUS_VALUES!r}")
