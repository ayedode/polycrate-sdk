from typing import Literal

ApiV1ProvidersListScope = Literal["system", "user"]

API_V1_PROVIDERS_LIST_SCOPE_VALUES: set[ApiV1ProvidersListScope] = {
    "system",
    "user",
}


def check_api_v1_providers_list_scope(value: str) -> ApiV1ProvidersListScope:
    if value in API_V1_PROVIDERS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_SCOPE_VALUES!r}")
