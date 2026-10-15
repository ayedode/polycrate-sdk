from typing import Literal

PatchedBlockRolloutConfigRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_STATE_VALUES: set[PatchedBlockRolloutConfigRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_patched_block_rollout_config_request_state(value: str) -> PatchedBlockRolloutConfigRequestState:
    if value in PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_ROLLOUT_CONFIG_REQUEST_STATE_VALUES!r}"
    )
