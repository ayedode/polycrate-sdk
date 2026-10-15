from typing import Literal

ProviderDetailScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

PROVIDER_DETAIL_SCS_IAAS_STATUS_VALUES: set[ProviderDetailScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_provider_detail_scs_iaas_status(value: str) -> ProviderDetailScsIaasStatus:
    if value in PROVIDER_DETAIL_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_SCS_IAAS_STATUS_VALUES!r}")
