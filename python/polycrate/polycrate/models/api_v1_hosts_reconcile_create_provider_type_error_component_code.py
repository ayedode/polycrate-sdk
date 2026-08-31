from typing import Literal

ApiV1HostsReconcileCreateProviderTypeErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateProviderTypeErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_reconcile_create_provider_type_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateProviderTypeErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
