from typing import Literal

ApiV1ProvidersListC5Status = Literal["none", "planned", "typ1", "typ2"]

API_V1_PROVIDERS_LIST_C5_STATUS_VALUES: set[ApiV1ProvidersListC5Status] = {
    "none",
    "planned",
    "typ1",
    "typ2",
}


def check_api_v1_providers_list_c5_status(value: str) -> ApiV1ProvidersListC5Status:
    if value in API_V1_PROVIDERS_LIST_C5_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_C5_STATUS_VALUES!r}")
