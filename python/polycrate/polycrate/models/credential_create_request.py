from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.credential_kind_enum import CredentialKindEnum, check_credential_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_create_request_secrets_type_0 import CredentialCreateRequestSecretsType0


T = TypeVar("T", bound="CredentialCreateRequest")


@_attrs_define
class CredentialCreateRequest:
    """Serializer for creating credentials via API (microservice integration).
    Allows setting all necessary fields for credential creation.

        Attributes:
            name (str):
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
                * `provider-account` - Provider Account Default: 'generic'.
            organization (None | Unset | UUID):
            workspace (None | Unset | UUID):
            api_endpoint (None | str | Unset):
            api_user (None | str | Unset):
            api_key (None | str | Unset):
            secrets (CredentialCreateRequestSecretsType0 | None | Unset): Credential secrets as JSON object (encrypted in
                database)
            kubeconfig (None | str | Unset):
            ssh_private_key (None | str | Unset):
            ssh_public_key (None | str | Unset):
            description (None | str | Unset):
            metadata (Any | Unset):
    """

    name: str
    kind: CredentialKindEnum | Unset = "generic"
    organization: None | Unset | UUID = UNSET
    workspace: None | Unset | UUID = UNSET
    api_endpoint: None | str | Unset = UNSET
    api_user: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    secrets: CredentialCreateRequestSecretsType0 | None | Unset = UNSET
    kubeconfig: None | str | Unset = UNSET
    ssh_private_key: None | str | Unset = UNSET
    ssh_public_key: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_create_request_secrets_type_0 import (
            CredentialCreateRequestSecretsType0,  # noqa: PLC0415
        )

        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        workspace: None | str | Unset
        if isinstance(self.workspace, Unset):
            workspace = UNSET
        elif isinstance(self.workspace, UUID):
            workspace = str(self.workspace)
        else:
            workspace = self.workspace

        api_endpoint: None | str | Unset
        if isinstance(self.api_endpoint, Unset):
            api_endpoint = UNSET
        else:
            api_endpoint = self.api_endpoint

        api_user: None | str | Unset
        if isinstance(self.api_user, Unset):
            api_user = UNSET
        else:
            api_user = self.api_user

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        secrets: dict[str, Any] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, CredentialCreateRequestSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        kubeconfig: None | str | Unset
        if isinstance(self.kubeconfig, Unset):
            kubeconfig = UNSET
        else:
            kubeconfig = self.kubeconfig

        ssh_private_key: None | str | Unset
        if isinstance(self.ssh_private_key, Unset):
            ssh_private_key = UNSET
        else:
            ssh_private_key = self.ssh_private_key

        ssh_public_key: None | str | Unset
        if isinstance(self.ssh_public_key, Unset):
            ssh_public_key = UNSET
        else:
            ssh_public_key = self.ssh_public_key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if organization is not UNSET:
            field_dict["organization"] = organization
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if api_endpoint is not UNSET:
            field_dict["api_endpoint"] = api_endpoint
        if api_user is not UNSET:
            field_dict["api_user"] = api_user
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if kubeconfig is not UNSET:
            field_dict["kubeconfig"] = kubeconfig
        if ssh_private_key is not UNSET:
            field_dict["ssh_private_key"] = ssh_private_key
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.credential_create_request_secrets_type_0 import (
            CredentialCreateRequestSecretsType0,  # noqa: PLC0415
        )

        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.organization, Unset):
            if isinstance(self.organization, UUID):
                files.append(("organization", (None, str(self.organization), "text/plain")))
            else:
                files.append(("organization", (None, str(self.organization).encode(), "text/plain")))

        if not isinstance(self.workspace, Unset):
            if isinstance(self.workspace, UUID):
                files.append(("workspace", (None, str(self.workspace), "text/plain")))
            else:
                files.append(("workspace", (None, str(self.workspace).encode(), "text/plain")))

        if not isinstance(self.api_endpoint, Unset):
            if isinstance(self.api_endpoint, str):
                files.append(("api_endpoint", (None, str(self.api_endpoint).encode(), "text/plain")))
            else:
                files.append(("api_endpoint", (None, str(self.api_endpoint).encode(), "text/plain")))

        if not isinstance(self.api_user, Unset):
            if isinstance(self.api_user, str):
                files.append(("api_user", (None, str(self.api_user).encode(), "text/plain")))
            else:
                files.append(("api_user", (None, str(self.api_user).encode(), "text/plain")))

        if not isinstance(self.api_key, Unset):
            if isinstance(self.api_key, str):
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))
            else:
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))

        if not isinstance(self.secrets, Unset):
            if isinstance(self.secrets, CredentialCreateRequestSecretsType0):
                files.append(("secrets", (None, json.dumps(self.secrets.to_dict()).encode(), "application/json")))
            else:
                files.append(("secrets", (None, str(self.secrets).encode(), "text/plain")))

        if not isinstance(self.kubeconfig, Unset):
            if isinstance(self.kubeconfig, str):
                files.append(("kubeconfig", (None, str(self.kubeconfig).encode(), "text/plain")))
            else:
                files.append(("kubeconfig", (None, str(self.kubeconfig).encode(), "text/plain")))

        if not isinstance(self.ssh_private_key, Unset):
            if isinstance(self.ssh_private_key, str):
                files.append(("ssh_private_key", (None, str(self.ssh_private_key).encode(), "text/plain")))
            else:
                files.append(("ssh_private_key", (None, str(self.ssh_private_key).encode(), "text/plain")))

        if not isinstance(self.ssh_public_key, Unset):
            if isinstance(self.ssh_public_key, str):
                files.append(("ssh_public_key", (None, str(self.ssh_public_key).encode(), "text/plain")))
            else:
                files.append(("ssh_public_key", (None, str(self.ssh_public_key).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_create_request_secrets_type_0 import (
            CredentialCreateRequestSecretsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        _kind = d.pop("kind", UNSET)
        kind: CredentialKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_credential_kind_enum(_kind)

        def _parse_organization(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization = _parse_organization(d.pop("organization", UNSET))

        def _parse_workspace(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_type_0 = UUID(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        workspace = _parse_workspace(d.pop("workspace", UNSET))

        def _parse_api_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_endpoint = _parse_api_endpoint(d.pop("api_endpoint", UNSET))

        def _parse_api_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_user = _parse_api_user(d.pop("api_user", UNSET))

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_secrets(data: object) -> CredentialCreateRequestSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = CredentialCreateRequestSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CredentialCreateRequestSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        def _parse_kubeconfig(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kubeconfig = _parse_kubeconfig(d.pop("kubeconfig", UNSET))

        def _parse_ssh_private_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_private_key = _parse_ssh_private_key(d.pop("ssh_private_key", UNSET))

        def _parse_ssh_public_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_public_key = _parse_ssh_public_key(d.pop("ssh_public_key", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        metadata = d.pop("metadata", UNSET)

        credential_create_request = cls(
            name=name,
            kind=kind,
            organization=organization,
            workspace=workspace,
            api_endpoint=api_endpoint,
            api_user=api_user,
            api_key=api_key,
            secrets=secrets,
            kubeconfig=kubeconfig,
            ssh_private_key=ssh_private_key,
            ssh_public_key=ssh_public_key,
            description=description,
            metadata=metadata,
        )

        credential_create_request.additional_properties = d
        return credential_create_request

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
