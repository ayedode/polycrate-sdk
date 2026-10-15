from typing import Literal

ApiV1PopsListEn50600Status = Literal["no", "planned", "unknown", "yes"]

API_V1_POPS_LIST_EN_50600_STATUS_VALUES: set[ApiV1PopsListEn50600Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_api_v1_pops_list_en_50600_status(value: str) -> ApiV1PopsListEn50600Status:
    if value in API_V1_POPS_LIST_EN_50600_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_EN_50600_STATUS_VALUES!r}")
