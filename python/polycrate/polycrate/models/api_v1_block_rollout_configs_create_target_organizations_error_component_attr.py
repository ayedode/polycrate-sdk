from typing import Literal

ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponentAttr = Literal["target_organizations"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponentAttr
] = {
    "target_organizations",
}


def check_api_v1_block_rollout_configs_create_target_organizations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateTargetOrganizationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_TARGET_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
