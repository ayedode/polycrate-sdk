from typing import Literal

ApiV1BlocksReconcileCreateVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_RECONCILE_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_reconcile_create_version_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateVersionErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
