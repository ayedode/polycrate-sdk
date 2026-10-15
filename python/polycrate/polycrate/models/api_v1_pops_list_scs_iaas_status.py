from typing import Literal

ApiV1PopsListScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

API_V1_POPS_LIST_SCS_IAAS_STATUS_VALUES: set[ApiV1PopsListScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_api_v1_pops_list_scs_iaas_status(value: str) -> ApiV1PopsListScsIaasStatus:
    if value in API_V1_POPS_LIST_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_SCS_IAAS_STATUS_VALUES!r}")
