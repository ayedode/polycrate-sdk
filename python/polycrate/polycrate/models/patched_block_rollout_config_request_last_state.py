from typing import Literal

PatchedBlockRolloutConfigRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_LAST_STATE_VALUES: set[PatchedBlockRolloutConfigRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_block_rollout_config_request_last_state(value: str) -> PatchedBlockRolloutConfigRequestLastState:
    if value in PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_LAST_STATE_VALUES!r}"
    )
