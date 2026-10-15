from typing import Literal

ApiV1PopsListIso27001Status = Literal["no", "planned", "unknown", "yes"]

API_V1_POPS_LIST_ISO_27001_STATUS_VALUES: set[ApiV1PopsListIso27001Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_api_v1_pops_list_iso_27001_status(value: str) -> ApiV1PopsListIso27001Status:
    if value in API_V1_POPS_LIST_ISO_27001_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_ISO_27001_STATUS_VALUES!r}")
