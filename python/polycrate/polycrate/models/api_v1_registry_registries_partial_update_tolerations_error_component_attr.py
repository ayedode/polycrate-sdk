from typing import Literal

ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_registry_registries_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
