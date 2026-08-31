from typing import Literal

ApiV1PopsReconcileCreateProviderEntityIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_POPS_RECONCILE_CREATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsReconcileCreateProviderEntityIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_pops_reconcile_create_provider_entity_id_error_component_code(
    value: str,
) -> ApiV1PopsReconcileCreateProviderEntityIdErrorComponentCode:
    if value in API_V1_POPS_RECONCILE_CREATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
