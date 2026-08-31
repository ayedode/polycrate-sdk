from typing import Literal

ApiV1CredentialsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_CREDENTIALS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1CredentialsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_credentials_list_created_by_component(value: str) -> ApiV1CredentialsListCreatedByComponent:
    if value in API_V1_CREDENTIALS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
