from typing import Literal

ApiV1RegistryRegistriesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_REGISTRY_REGISTRIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_registry_registries_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
