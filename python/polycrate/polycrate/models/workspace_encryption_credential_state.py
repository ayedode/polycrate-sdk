from typing import Literal

WorkspaceEncryptionCredentialState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

WORKSPACE_ENCRYPTION_CREDENTIAL_STATE_VALUES: set[WorkspaceEncryptionCredentialState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_workspace_encryption_credential_state(value: str) -> WorkspaceEncryptionCredentialState:
    if value in WORKSPACE_ENCRYPTION_CREDENTIAL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_ENCRYPTION_CREDENTIAL_STATE_VALUES!r}")
