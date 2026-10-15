from typing import Literal

ApiV1ProvidersListScsIaasStatus = Literal["compatible", "listed_not_certified", "none"]

API_V1_PROVIDERS_LIST_SCS_IAAS_STATUS_VALUES: set[ApiV1ProvidersListScsIaasStatus] = {
    "compatible",
    "listed_not_certified",
    "none",
}


def check_api_v1_providers_list_scs_iaas_status(value: str) -> ApiV1ProvidersListScsIaasStatus:
    if value in API_V1_PROVIDERS_LIST_SCS_IAAS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_SCS_IAAS_STATUS_VALUES!r}")
