from typing import Literal

ApiV1BlocksReconcileCreateChecksumErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_RECONCILE_CREATE_CHECKSUM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateChecksumErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_reconcile_create_checksum_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateChecksumErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CHECKSUM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CHECKSUM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
