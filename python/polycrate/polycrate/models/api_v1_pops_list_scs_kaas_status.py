from typing import Literal

ApiV1PopsListScsKaasStatus = Literal["compatible", "listed_not_certified", "none"]

API_V1_POPS_LIST_SCS_KAAS_STATUS_VALUES: set[ApiV1PopsListScsKaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_api_v1_pops_list_scs_kaas_status(value: str) -> ApiV1PopsListScsKaasStatus:
    if value in API_V1_POPS_LIST_SCS_KAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_SCS_KAAS_STATUS_VALUES!r}")
