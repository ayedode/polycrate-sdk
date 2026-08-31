from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_kind_enum import CredentialKindEnum, check_credential_kind_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalCredential")


@_attrs_define
class ExternalCredential:
    """Serializer for creating/retrieving Credentials via the external API endpoint.

    Intended for System API Keys and Org API Keys to manage dns-provider
    credentials. Sensitive fields (api_key) are write-only — never returned.

    Spec 491: Credential API Endpoint

        Attributes:
            id (UUID):
            name (str):
            organization_id (UUID): UUID of the Organization this credential belongs to. Required. Org API Key users can
                only set their own organization.
            created_at (datetime.datetime):
            kind (CredentialKindEnum | Unset): * `api-key` - API Key
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
            api_user (None | str | Unset):
            metadata (Any | Unset):
    """

    id: UUID
    name: str
    organization_id: UUID
    created_at: datetime.datetime
    kind: CredentialKindEnum | Unset = UNSET
    api_user: None | str | Unset = UNSET
    metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        organization_id = str(self.organization_id)

        created_at = self.created_at.isoformat()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        api_user: None | str | Unset
        if isinstance(self.api_user, Unset):
            api_user = UNSET
        else:
            api_user = self.api_user

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization_id": organization_id,
                "created_at": created_at,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if api_user is not UNSET:
            field_dict["api_user"] = api_user
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        organization_id = UUID(d.pop("organization_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        _kind = d.pop("kind", UNSET)
        kind: CredentialKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_credential_kind_enum(_kind)

        def _parse_api_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_user = _parse_api_user(d.pop("api_user", UNSET))

        metadata = d.pop("metadata", UNSET)

        external_credential = cls(
            id=id,
            name=name,
            organization_id=organization_id,
            created_at=created_at,
            kind=kind,
            api_user=api_user,
            metadata=metadata,
        )

        external_credential.additional_properties = d
        return external_credential

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
