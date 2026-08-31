from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.credential_kind_enum import CredentialKindEnum, check_credential_kind_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalCredentialRequest")


@_attrs_define
class ExternalCredentialRequest:
    """Serializer for creating/retrieving Credentials via the external API endpoint.

    Intended for System API Keys and Org API Keys to manage dns-provider
    credentials. Sensitive fields (api_key) are write-only — never returned.

    Spec 491: Credential API Endpoint

        Attributes:
            name (str):
            organization_id (UUID): UUID of the Organization this credential belongs to. Required. Org API Key users can
                only set their own organization.
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
            api_key (None | str | Unset): Provider API token or secret. Write-only — never returned in responses.
            api_user (None | str | Unset):
            metadata (Any | Unset):
    """

    name: str
    organization_id: UUID
    kind: CredentialKindEnum | Unset = UNSET
    api_key: None | str | Unset = UNSET
    api_user: None | str | Unset = UNSET
    metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        organization_id = str(self.organization_id)

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

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
                "name": name,
                "organization_id": organization_id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_user is not UNSET:
            field_dict["api_user"] = api_user
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("organization_id", (None, str(self.organization_id), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.api_key, Unset):
            if isinstance(self.api_key, str):
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))
            else:
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))

        if not isinstance(self.api_user, Unset):
            if isinstance(self.api_user, str):
                files.append(("api_user", (None, str(self.api_user).encode(), "text/plain")))
            else:
                files.append(("api_user", (None, str(self.api_user).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        organization_id = UUID(d.pop("organization_id"))

        _kind = d.pop("kind", UNSET)
        kind: CredentialKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_credential_kind_enum(_kind)

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_api_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_user = _parse_api_user(d.pop("api_user", UNSET))

        metadata = d.pop("metadata", UNSET)

        external_credential_request = cls(
            name=name,
            organization_id=organization_id,
            kind=kind,
            api_key=api_key,
            api_user=api_user,
            metadata=metadata,
        )

        external_credential_request.additional_properties = d
        return external_credential_request

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
