from typing import Literal

PatchedArtifactRequestScope = Literal["system", "user"]

PATCHED_ARTIFACT_REQUEST_SCOPE_VALUES: set[PatchedArtifactRequestScope] = {
    "system",
    "user",
}


def check_patched_artifact_request_scope(value: str) -> PatchedArtifactRequestScope:
    if value in PATCHED_ARTIFACT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ARTIFACT_REQUEST_SCOPE_VALUES!r}")
