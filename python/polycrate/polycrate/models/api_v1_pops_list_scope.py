from typing import Literal

ApiV1PopsListScope = Literal["system", "user"]

API_V1_POPS_LIST_SCOPE_VALUES: set[ApiV1PopsListScope] = {
    "system",
    "user",
}


def check_api_v1_pops_list_scope(value: str) -> ApiV1PopsListScope:
    if value in API_V1_POPS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_SCOPE_VALUES!r}")
