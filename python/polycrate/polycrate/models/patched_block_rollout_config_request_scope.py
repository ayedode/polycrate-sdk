from typing import Literal

PatchedBlockRolloutConfigRequestScope = Literal["system", "user"]

PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_SCOPE_VALUES: set[PatchedBlockRolloutConfigRequestScope] = {
    "system",
    "user",
}


def check_patched_block_rollout_config_request_scope(value: str) -> PatchedBlockRolloutConfigRequestScope:
    if value in PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_SCOPE_VALUES!r}"
    )
