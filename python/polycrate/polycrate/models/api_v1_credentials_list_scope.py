from typing import Literal

ApiV1CredentialsListScope = Literal["system", "user"]

API_V1_CREDENTIALS_LIST_SCOPE_VALUES: set[ApiV1CredentialsListScope] = {
    "system",
    "user",
}


def check_api_v1_credentials_list_scope(value: str) -> ApiV1CredentialsListScope:
    if value in API_V1_CREDENTIALS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_SCOPE_VALUES!r}")
