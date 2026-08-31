from typing import Literal

ApiV1ProvidersListKind = Literal["hardware", "infrastructure", "software"]

API_V1_PROVIDERS_LIST_KIND_VALUES: set[ApiV1ProvidersListKind] = {
    "hardware",
    "infrastructure",
    "software",
}


def check_api_v1_providers_list_kind(value: str) -> ApiV1ProvidersListKind:
    if value in API_V1_PROVIDERS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_KIND_VALUES!r}")
