from typing import Literal

ApiV1PopsListC5Status = Literal["none", "planned", "typ1", "typ2"]

API_V1_POPS_LIST_C5_STATUS_VALUES: set[ApiV1PopsListC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_api_v1_pops_list_c5_status(value: str) -> ApiV1PopsListC5Status:
    if value in API_V1_POPS_LIST_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_C5_STATUS_VALUES!r}")
