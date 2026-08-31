from typing import Literal

ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_RECONCILE_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_reconcile_create_changelog_poly_raw_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateChangelogPolyRawErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_CHANGELOG_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
