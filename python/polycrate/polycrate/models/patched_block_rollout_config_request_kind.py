from typing import Literal

PatchedBlockRolloutConfigRequestKind = Literal["config", "trigger"]

PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_KIND_VALUES: set[PatchedBlockRolloutConfigRequestKind] = {
    "config",
    "trigger",
}


def check_patched_block_rollout_config_request_kind(value: str) -> PatchedBlockRolloutConfigRequestKind:
    if value in PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_KIND_VALUES!r}")
