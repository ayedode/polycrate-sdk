from typing import Literal

ApiV1RegistryRegistriesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_REGISTRY_REGISTRIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_registry_registries_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
