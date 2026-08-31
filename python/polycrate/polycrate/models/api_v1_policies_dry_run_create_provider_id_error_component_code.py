from typing import Literal

ApiV1PoliciesDryRunCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_policies_dry_run_create_provider_id_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateProviderIdErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
