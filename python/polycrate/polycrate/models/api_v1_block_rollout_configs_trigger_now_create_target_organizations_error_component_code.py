from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_block_rollout_configs_trigger_now_create_target_organizations_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
