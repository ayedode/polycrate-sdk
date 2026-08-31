from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_kind_enum import CredentialKindEnum, check_credential_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

T = TypeVar("T", bound="WorkspaceEncryptionCredential")


@_attrs_define
class WorkspaceEncryptionCredential:
    """Serializer for workspace encryption credentials - includes SSH keys for CLI.

    Attributes:
        id (UUID):
        name (str):
        kind (CredentialKindEnum): * `api-key` - API Key
            * `kubeconfig` - Kubeconfig
            * `s3-credential` - S3 Credential
            * `ssh-keys` - SSH Keys
            * `generic` - Generic
            * `webhook` - Webhook
            * `agent_token` - Agent Token
            * `workspace-encryption` - Workspace Encryption
            * `oci-registry-credential` - OCI Registry Credential
            * `helm-repository-credential` - Helm Repository Credential
            * `apmstack-metrics-credential` - APM Stack Metrics Credential
            * `unified-apm-credential` - Unified APM Credential
            * `unified-registry-credential` - Unified Registry Credential
            * `apmstack-logs-credential` - APM Stack Logs Credential
            * `apmstack-traces-credential` - APM Stack Traces Credential
            * `domain-auth-code` - Domain Auth Code
            * `dns-provider` - DNS Provider
            * `system_api_key` - System API Key
            * `org_api_key` - Org API Key
            * `controlplane-token` - Controlplane Token
            * `provider-account` - Provider Account
        ssh_private_key (None | str):
        ssh_public_key (None | str):
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
    """

    id: UUID
    name: str
    kind: CredentialKindEnum
    ssh_private_key: None | str
    ssh_public_key: None | str
    state: LastStateEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        ssh_private_key: None | str
        ssh_private_key = self.ssh_private_key

        ssh_public_key: None | str
        ssh_public_key = self.ssh_public_key

        state: str = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "ssh_private_key": ssh_private_key,
                "ssh_public_key": ssh_public_key,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_credential_kind_enum(d.pop("kind"))

        def _parse_ssh_private_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ssh_private_key = _parse_ssh_private_key(d.pop("ssh_private_key"))

        def _parse_ssh_public_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ssh_public_key = _parse_ssh_public_key(d.pop("ssh_public_key"))

        state = check_last_state_enum(d.pop("state"))

        workspace_encryption_credential = cls(
            id=id,
            name=name,
            kind=kind,
            ssh_private_key=ssh_private_key,
            ssh_public_key=ssh_public_key,
            state=state,
        )

        workspace_encryption_credential.additional_properties = d
        return workspace_encryption_credential

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
