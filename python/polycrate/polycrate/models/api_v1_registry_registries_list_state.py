from typing import Literal

ApiV1RegistryRegistriesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_REGISTRY_REGISTRIES_LIST_STATE_VALUES: set[ApiV1RegistryRegistriesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_registry_registries_list_state(value: str) -> ApiV1RegistryRegistriesListState:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_STATE_VALUES!r}")
