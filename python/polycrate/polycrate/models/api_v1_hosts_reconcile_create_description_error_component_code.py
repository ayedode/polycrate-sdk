from typing import Literal

ApiV1HostsReconcileCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_reconcile_create_description_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateDescriptionErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
