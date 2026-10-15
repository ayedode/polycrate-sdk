from typing import Literal

ProviderDetailRequestScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

PROVIDER_DETAIL_REQUEST_SCS_IAAS_STATUS_VALUES: set[ProviderDetailRequestScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_provider_detail_request_scs_iaas_status(value: str) -> ProviderDetailRequestScsIaasStatus:
    if value in PROVIDER_DETAIL_REQUEST_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_SCS_IAAS_STATUS_VALUES!r}")
