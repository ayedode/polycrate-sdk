from typing import Literal

ApiV1RegistryRegistriesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_REGISTRY_REGISTRIES_LIST_STATE_NOT_VALUES: set[ApiV1RegistryRegistriesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_registry_registries_list_state_not(value: str) -> ApiV1RegistryRegistriesListStateNot:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_STATE_NOT_VALUES!r}")
